from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from requests import request
from whoosh import query

from bookclass.models import tpress, tbook
from .models import Users
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, logout, login
# 分页库
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def users(request):
    return None


# 首页
def index(requset):
    # 获取全部教材
    all_book = tbook.objects.all()
    print(all_book.count())

    gong_book = all_book.filter(p_id=1).order_by('-praise', '-comment', 'price')[:10]
    li_book = all_book.filter(p_id=4).order_by('-praise', '-comment', 'price')[:10]
    jing_book = all_book.filter(p_id=2).order_by('-praise', '-comment', 'price')[:10]
    yi_book = all_book.filter(p_id=3).order_by('-praise', '-comment', 'price')[:10]

    context = {
        'all_book': all_book,       # 所有教材
        'gong_book': gong_book,     # 工学教材推荐
        'li_book': li_book,         # 理学教材推荐
        'jing_book': jing_book,     # 经济管理教材推荐
        'yi_book': yi_book,         # 医学教材推荐
    }

    return render(requset, 'index.html', context)


# 注册页面
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 实例化
        user_register_form = UserRegisterForm(request.POST)
        # 判断账号密码是否合法
        if user_register_form.is_valid():
            username = user_register_form.cleaned_data['username']
            password = user_register_form.cleaned_data['password']
            email = user_register_form.cleaned_data['email']
            college = user_register_form.cleaned_data['college']

            # 拿到usename和password后，到数据库中存储账号密码的数据表中找一遍
            user_list = Users.objects.filter(Q(username=username))
            # 如果表中已存在当前username
            if user_list:
                # 提示返回登录页面登录
                return render(request, 'register.html', {
                    'msg': '当前用户已存在！请返回登录！'
                })
            else:  # 表中不存在当前username，则直接注册
                a = Users()  # models.py中的Users类,相当于表
                # 注册账号密码
                a.username = username
                a.set_password(password)
                a.email = email
                a.college = college
                a.save()
                return redirect(reverse('user_login'))
        else:  # 验证不通过
            return render(request, 'register.html', {
                'user_register_form': user_register_form
            })


# 登录页面
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:  # 接收到POST请求
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():  # 判断是否合法
            username = user_login_form.cleaned_data['username']  # 获取页面传输过来的账户
            password = user_login_form.cleaned_data['password']  # 获取页面传输过来的密码
            # 登录验证
            user = authenticate(username=username, password=password)  # 提供用户认证，验证当前账号密码是否正确
            # 判断
            if user:  # 找到对象不为空
                login(request, user)
                return redirect(reverse('index'))
            else:
                return render(request, 'login.html', {
                    # 提示错误信息
                    'msg': '账号或密码有误！请检查！'
                })
        else:
            return render(request, 'login.html', {
                'user_login_form': user_login_form
            })


# 用户个人中心
def user_info(request):
    return render(request, 'usercenter-info.html')


# 修改密码
def pwd_reset(request):
    state = None
    user = request.user  # 获取当前用户
    if request.method == 'POST':  # 判断当前请求
        old_password = request.POST.get('old_password', '')  # 原始密码
        new_password = request.POST.get('new_password', '')  # 新密码
        new_passwords = request.POST.get('new_passwords', '')  # 再次确认密码
        # 匹配数据库里的密文时，需要通过check_password()来验证
        if user.check_password(old_password):  # 将用户输入的原始密码与数据库中用户对应的密码进行验证
            if not new_password:  #
                state = 'empty'
            elif new_password != new_passwords:  # 若两次输入的密码不一致
                state = '两次密码输入不一致！'
            else:  # 两次密码输入一致
                user.set_password(new_password)  # 获取到用户输入的新密码
                user.save()  # 保存并更新到后台数据库中
                state = 'success'  # 状态码
        else:
            state = '原始密码输入错误'
        return render(request, 'login.html')  # 密码修改成功后，跳转到登录界面重新登录
    content = {
        'user': user,
        'active_menu': user_info,
        'state': state
    }
    return render(request, 'password_reset.html', content)  # 定向到修改密码界面


# 退出登录
def user_logout(request):
    logout(request)
    return redirect(reverse('user_login'))


# 密码重置
def user_reset(request):
    return render(request, 'password_reset.html')


###################### 后台管理首页仪表板 ##################################
def dashboard(request):
    """
    将后台管理首页仪表板定向到指定页面
    :param request:
    :return:
    """

    # 统计当前系统已注册用户数量
    user_count = Users.objects.count()
    context = {
        'user_count': user_count
    }
    # 重定向到仪表板页面
    return render(request, 'dashboard.html', context)


#######################  自定义搜索功能  ################################################3

from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet


# 搜索结果自定义
class BookSearchView(SearchView):
    """
        搜索结果自定义
    """
    # context_object_name = 'articles'
    paginate_by = 8  # 每条最多显示8条数据

    # haystack文档解释 https://django-haystack.readthedocs.io/en/v2.4.1/searchqueryset_api.html
    queryset = SearchQuerySet()  # 旨在使执行搜索和迭代其结果变得容易且一致

    # 根据选择展示对应教材
    def get_queryset(self):
        # get_queryset：返回一个定制的对象
        qs = super(BookSearchView, self).get_queryset()
        # 输出总数
        print(len(qs))
        # 获取教材
        con_books = self.request.GET.get('con_books', '')
        # 获取出版社
        press = self.request.GET.get('press', '')

        # 类似于QuerySet 对象。适合用filter、all、excluet方法，但是不支持get。只支持在索引字段操作,而且不能使用__contains
        if press:  # 若出版社不为空
            qs = qs.filter(press=press)
        # 当con_books存在,将教材结果数据进行筛选
        if con_books:
            qs = qs.exclude(text='高职')
            # 点击评论数时
            if con_books == "comment":
                qs = qs.order_by('-' + con_books)
            # 点击好评率时
            if con_books == "praise":
                qs = qs.order_by('-' + con_books)
            # 点击价格时
            if con_books == "price":
                qs = qs.order_by(con_books)
            # 点击规划教材时
            if con_books == "guihua":
                qs = qs.filter(text='规划').exclude(text='高职')

        return qs

    def get_context_data(self, *args, **kwargs):
        books = self.request.GET.get('con_books', '')
        press = self.request.GET.get('press', '')  # 获取出版社

        # super() 函数是用于调用父类(超类)的一个方法。用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
        #         但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
        context = super(BookSearchView, self).get_context_data(*args, **kwargs)

        context.update({"page": context.pop("page_obj"),
                        "con_books": books,
                        "current_press": press, })

        # 推荐 —— 猜你喜欢
        guess = self.get_guess(context['page'][0].object.p_id)
        context.update({"guess": guess})
        return context

    def get_guess(self, id):
        """
        推荐 —— 猜你喜欢
        判断当前的搜索关键词属于哪个学科下的教材，并按学科推荐 好评率、评论数、价格 前4 的教材
        :param id:
        :return:
        """

        # 获取全部教材
        allbooks = tbook.objects.all()
        # 若有搜索结果且获取到学科id,获取该学科下全部数据；否则不查询，在全部教材中推荐
        if id:
            allbooks = allbooks.filter(p_id=id)

        # 按学科推荐 好评率、评论数、价格 前4 的教材
        praise = allbooks.order_by('-praise')
        if praise.count() > 4:
            praise = praise[:4]
        # print(praise)

        comment = allbooks.order_by('-comment')
        if comment.count() > 4:
            comment = comment[:4]

        price = allbooks.order_by('price')
        if price.count() > 4:
            price = price[:4]
        res = {
            # 好评率
            'praise': praise,
            # 评论数
            'comment': comment,
            # 价格
            'price': price,
        }
        return res
