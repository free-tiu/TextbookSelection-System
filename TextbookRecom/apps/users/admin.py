from django.contrib import admin

# Register your models here.
from .models import *

#
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'last_login', 'is_superuser', 'email', 'college', 'password']
    # 设置按照id排序（从小到大），从大到小为'-id'
    ordering = ('id',)
    # 设置列表每页最多小时个数，默认100
    # list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    # list_editable 设置默认可编辑字段
    # list_editable = ['username', 'password']

# 将模型注册到后台
admin.site.register(Users,UserProfileAdmin)

# 修改网页标题和头部标题
admin.site.site_title = '系统后台管理'
admin.site.site_header = '系统后台管理'


