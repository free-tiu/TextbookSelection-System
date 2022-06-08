# 分页库
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse
# 规划教材
from .models import tbook, tpress


########################################################################################################################
# 按照是否为规划进行排序
def guihua_book(request):
    # 获取所有的出版社分类数据
    all_press = tpress.objects.all()

    # 使用模糊查询 —— 查询书名中包含有”规划“二字的教材,并且将高职相关数据过滤掉
    book_guihua = tbook.objects.filter(name__contains='规划').exclude(name__contains='高职')

    # 分页功能
    pagenum = request.GET.get('pagenum', '1')  # 获取页码，默认第一页 可以为‘’
    # 实例化分页库   Paginator(需要分页的数据all_book,每页分几条数据40,)
    pa = Paginator(book_guihua, 12)

    # 获取当前请求的页码号
    page_number = pagenum
    # 获取分页后的总数
    total_pages = pa.num_pages

    # 尝试拿取数据
    try:
        pages = pa.page(pagenum)  # paginator.page(页码数)获取
    except PageNotAnInteger:  # 第一页
        pages = pa.page(1)
    except EmptyPage:  # 最后一页
        pages = pa.page(pa.num_pages)  # num_pages总页数

    con = {
        'all_press': all_press,
        'book_guihua': book_guihua,  # 规划教材
        'pages': pages,  # 分页规划教材
        'page_number': page_number,  # 获取当前请求的页码号
        'total_pages': total_pages,  # 获取总页数
    }
    return render(request, 'gh_book.html', con)


########################################################################################################################


