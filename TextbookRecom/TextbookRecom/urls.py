"""TextbookRecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from users import views
from users.views import index, user_login
from users.views import BookSearchView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 分发路由
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('bookclass/', include(('bookclass.urls', 'bookclass'), namespace='bookclass')),
    path('operations/', include(('operations.urls', 'operations'), namespace='operations')),
    # 注册index页面
    path('index/', index, name='index'),
    path('', user_login, name='user_login'),

    path('search/', BookSearchView.as_view()),  # 全文检索

    # path('search/', include("haystack.urls")),  # 全文检索
]
