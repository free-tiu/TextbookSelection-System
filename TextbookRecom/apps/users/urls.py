
from django.contrib import admin
from django.urls import path

from users import views
from users.views import index, pwd_reset
from users.views import user_login, register, user_logout, user_info, user_reset

app_name = 'urls'


urlpatterns = [
    # 分发路由
    path('users/', views.users, name='users'),
    # 系统首页
    path('index/', index, name='index'),
    # 登录
    path('', user_login, name='user_login'),
    # 注册
    path('register/', register, name='register'),
    # 退出
    path('logout/', user_logout, name='user_logout'),
    # 密码重置
    path('password_reset/', user_reset, name='user_reset'),

    # 用户个人中心
    path('user_info/', user_info, name='user_info'),

    # 修改密码
    path('pwd_reset/', pwd_reset, name='pwd_reset'),

    # 仪表板面
    path('dashboard/', views.dashboard, name='dashboard'),

]
