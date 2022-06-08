from django.contrib import admin

# Register your models here.
from .models import tbook, tpress

# 注册tbook表
@admin.register(tbook)
class UserProfileAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ['id', 'src', 'name', 'press', 'author', 'date', 'comment', 'praise', 'price', 'b_href']
    # 设置按照id排序（从小到大），从大到小为'-id'
    ordering = ('id',)
    # 设置列表每页最多小时个数，默认100
    # list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    # 设置某一字段在编辑页面不可见（即无法编辑）
    exclude = ('id',)
    #list_editable 设置默认可编辑字段
    # list_editable = ['src', 'name', 'press', 'author', 'date']
    # 参与搜索的字段
    search_fields = ['name', 'press', 'author']

# 注册tpress表 —— 出版社表
# @admin.register(tpress)
# class UserProfileAdmin(admin.ModelAdmin):
#     # 列表显示字段
#     list_display = ['id', 'p_id', 'p_name', 'p_src']
#     # 设置按照id排序（从小到大），从大到小为'-id'
#     ordering = ('id',)
#     # 设置列表每页最多小时个数，默认100
#     # list_per_page = 50
#     actions_on_top = True
#     actions_on_bottom = True
#     # 设置某一字段在编辑页面不可见（即无法编辑）
#     # exclude = ('id',)
#
#     # 参与搜索的字段
#     search_fields = ['p_name']
#     # 设置默认可编辑字段
#     # list_editable = ['p_name']



# 注册表
# admin.site.register(tbook,UserProfileAdmin)

# 注册tclass表 —— 学科分类
# @admin.register(tclass)
# class UserProfileAdmin(admin.ModelAdmin):
#     # 列表显示字段
#     list_display = ['id', 'c_name', 'c_src']
#     # 设置按照id排序（从小到大），从大到小为'-id'
#     ordering = ('id',)
#     # 设置列表每页最多小时个数，默认100
#     # list_per_page = 50
#     actions_on_top = True
#     actions_on_bottom = True
#     # 设置某一字段在编辑页面不可见（即无法编辑）
#     # exclude = ('id',)
#
# # 注册表
# # admin.site.register(tclass,UserProfileAdmin)


# 注册表
# admin.site.register(tpress,UserProfileAdmin)


