## settings中修改数据库驱动
```python
DATABASES = {
    'default': {
        # 表示数据库的引擎（使用MySQL数据库时，修改该参数为’django.db.backends.mysql‘）
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dangdang',   # 访问MySQL的数据库的名称
        'USER': 'root',     # 数据库用户名
        'PASSWORD': 'root',     # 数据库密码
        'HOST': '127.0.0.1',    # 数据库服务器地址
        'PORT': '3306',     # 数据库服务器端口号

    }
}
```

### 解决mysql自增长id不从1开始
```
truncate table 表名;
```

## 创建项目
django-admin startproject 项目名
## 创建应用
python3 nanage.py startapp 应用名
## 注册应用
- 将新创建的应用注册到settings.py文件中的`INSTLLED_APPS`中

## 迁移数据库
```
## ①
    工具栏‘Tool’ 
=> 'Run manage.py Task'
=>  migrate 

## ②
#生成迁移文件
python3 manage.py makemigrations
# 执行迁移
python3 manage.py migrate
```

## 创建管理员项目
python3 manage.py createsuperuser

## 运行项目
python3 manage.py runserver 8080

## 虚拟环境
### 创建虚拟环境
python -m venv venv
### 进入虚拟环境
#### win
venv/Script/activate
#### Ubuntu
source venv/bin/active
### 关闭虚拟环境
deactivate


## 运行报错
### MySQL数据库相关
- 在新建的项目的`__init__.py`文件中添加如下：
```python
import pymysql
pymysql.install_as_MySQLdb()
```

## 运行h5页面
### 引用静态页面
- 在`setting.py`中添加如下代码
```python
# Static files (CSS, JavaScript, Images)    =>  静态文件
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# 默认只有'/static/'，需要在后面加上 ’static/‘
STATIC_URL = '/static/'
# 列表
STATICFILES_DIRS = [
    BASE_DIR / "static",
    ## 定义的是项目所在的完整路径
    # 需要在项目根路径下创建一个名为”static“的目录
    os.path.join(BASE_DIR,'/static/'),    
    ## 自定义路径
    '/文件夹/文件夹/文件夹/',
]
## 后加
STATIC_ROOT = os.path.join(BASE_DIR,'statics')
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR,'templates')
]
```
- 在与app项目同级的目录下创建`static`文件夹
    - 后再新建的文件夹中创建`css`文件夹，存放css文件
## 更改时区
- 在`settings.py`中找到相关
```python
LANGUAGE_CODE = 'zh-hans'   #网页默认中文显示

TIME_ZONE = 'Asia/Shanghai'
```

## 语言模板基础
### 1、表达式插值

#### 单个变量
``````html
<!-- 单个变量 -->
{{ variable }}
``````
#### 获取字典的键或对象的属性
``````html
<!-- 获取字典的键或对象的属性 -->
{{ dict.key }}
{{ object.attribute }}
``````
#### 获取列表中的某个元素
``````html
<!-- 获取列表中的某个元素 -->
{{ list.0 }}
``````
#### 示例
``````html
<h1>{{ name }}</h1>
<p>{{ news.title }}</p>
<p>{{ news.visitors.0 }}</p>
``````
----
### 2、条件语句
```
如果变量 is_true 为真，
那么最终渲染出来的就是 
    <h1>It is true!</h1>，
否则就是 
    <h1>It is false!</h1>。
```
- 注意
  - 整个条件语句必须以 {% endif %} 结束，并且 {% else %} 是可选的。
``````html
{% if is_true %}
  <h1>It is true!</h1>
{% else %}
  <h1>It is false!</h1>
{% endif %}
``````
----
### 3、循环语句
``````html
{% for elem in some_list %}
  <p>{{ elem }}</p>
{% endfor %}
``````
---
## 与数据库联动
### ORM
- model.py
```python
# 查询所有模型
# 等价于 SELECT * FROM Blog
Blog.objects.all()

# 查询单个模型
# 等价于 SELECT * FROM Blog WHERE ID=1
Blog.objects.get(id=1)

# 添加单个模型
# 等价于 INSERT INTO Blog (title, content) VALUES ('hello', 'world')
blog = Blog(title='hello', content='world')
blog.save()
```
### 创建数据表
- 在 `models.py` 中添加：
```python
from django.db import models

# Post相当于数据表名
class Post(models.Model):
    # title 为数据表中的一个字段
    title = models.CharField(max_length=200)
    # content 为数据表中的一个字段
    content = models.TextField()

    def __str__(self):
        return self.title
```
### 配置后台管理接口
#### 在视图中添加数据查询
- 在视图文件中添加从数据库中查询的代码
``````python
from django.shortcuts import render
from .models import Post

def index(request):
    content = { 'news_list': Post.objects.all() }
    return render(request, 'news/index.html', content=content)
``````
----
## 页面复用
### 继承标签
``````python
{% extends "页面.html" %}
``````
#### 动态内容生命标签
- block 和 endblock 是故定标签语句
- content 可以自定义命名
``````python
{% block content %}
{% endblock %}
``````

## 创建数据表
### 创建数据表的同时设置默认值

```
null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空，
    那么在新建一个model对象的时候是不会报错的！！

blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，
    比如 admin 界面下增加 model 一条记录的时候。直观的看到就是该字段不是粗体。
```


## 注册model模型

## admin配置
### 调整页面头部显示和页面页面标题
```python
class MyAdminSite(admin.AdminSite):
    site_header = '教材选用资源管理系统'  # 设置页面显示标题
    site_title = '教材选用系统'   # 设置页面头部标题
admin_site = MyAdminSite(name='management')
```

## admin相关设置（示例）
```python
# 设置在列表中显示的字段，id为django模型默认的主键
list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'create_time')
# 设置在列表可编辑字段
list_editable = ('status', 'qq')
# 设置通过点击某一字段可跳转至修改页面
list_display_links = ('name', 'id')
# 设置按照某一字段可搜索
search_fields = ('name', 'email', 'qq', 'phone')
# 设置按照某一字段过滤
list_filter = ('sex', 'status', 'create_time')
# 设置按照id排序（从小到大），从大到小为'-id'
ordering = ('id',)
# 按照更详细的时间分类
date_hierarchy = 'create_time'
# 设置列表每页最多小时个数，默认100
list_per_page = 50
# 在编辑页面使字段分块，自定义哪些字段在同一行
fieldsets = (('基础信息', {'fields': ('name', 'sex', 'profession')}),
             ('联系方式', {'fields': ('email', 'qq', 'phone')}),
             ('审核结果', {'fields': ('status',)})
             )

show_full_result_count = True
# 列表页面动作那一栏页面顶部和底部都显示
actions_on_top = True
actions_on_bottom = True
# 设置某一字段在编辑页面不可见（即无法编辑）
exclude = ('name', )
# 在编辑页面只对指定字段进行编辑和exclude效果相反
fields = ('name', )
# 添加页面标题和头部标题
class MyAdminSite(admin.AdminSite):
    # 添加页面显示标题
    site_header = "学员管理系统"
    # 设置页面头部标题
    site_title = "学员运维系统"
# 修改完页面标题和页面头部标题后，需要在urls.py里面也做相应的修改
admin_site = MyAdminSite(name='management')
admin_site.register(Student, StudentAdmin)
# 用这个修改好像更简单，不用专门写一个类来继承AdminSite，也不需用在urls.py里面做修改
admin.site.site_header = "学员管理系统"
admin.site.site_title = "学员运维系统"
# 为了能够使得依然有权限管理，下面这句还需依然保留
admin.site.register(Student, StudentAdmin)

```

## 重新生成索引文件
```
python manage.py rebuild_index
```

## 修改密码
```
# from django.contrib.auth.models import User
# user=User.objects.get(username='XXX')
# user.set_password('new_password')
# user.save()
```


## 生成依赖文件
```
pip3 freeze > requirements.txt
```
