from django.urls import path

from bookclass.views import guihua_book

app_name = 'bookclass'

urlpatterns = [
    # 系统首页
    # path('',index,name='index'),


    # 规划教材
    path('guihua_book/', guihua_book, name='guihua_book'),

]
