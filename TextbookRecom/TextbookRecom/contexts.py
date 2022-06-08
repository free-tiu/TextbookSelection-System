"""
    全局变量
"""

from django.conf import settings
from django.shortcuts import render

from bookclass.models import tbook, tpress


def lang(request):
    # 获取出版社数据
    allpress = tpress.objects.all()
    # 获取教材信息数据
    allbook = tbook.objects.all()

    # 出版社选择
    nowpress = request.GET.get('press', '')
    # 判断now_press是否存在
    if nowpress:
        allbook = allbook.filter(press=nowpress)

    # 分类筛选排序
    con_books = request.GET.get('books', '')
    # 判断books是否存在
    if con_books:
        allbook = allbook.order_by('-' + con_books)  # 在base.html 将books参数传值过来，然后在赋值给all_book

    return locals()












