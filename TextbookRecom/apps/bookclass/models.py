from django.db import models

# 教材表
class tbook(models.Model):
    src = models.ImageField(upload_to='user/', max_length=200, verbose_name="教材图片", null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name="教材名称", null=True, blank=True)
    press = models.CharField(max_length=11, verbose_name="出版社", null=True, blank=True)
    author = models.CharField(max_length=200, verbose_name="作者", null=True, blank=True)
    date = models.CharField(max_length=200, verbose_name="出版时间", null=True, blank=True)
    b_href = models.CharField(max_length=200, verbose_name="详情页链接", null=True, blank=True)
    comment = models.IntegerField(verbose_name="教材评论数", null=True, blank=True)
    praise = models.IntegerField(verbose_name="好评率", null=True, blank=True)
    price = models.CharField(max_length=200, verbose_name="价格", null=True, blank=True)
    p_id = models.IntegerField(verbose_name="学科id", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '教材列表'
        verbose_name_plural = verbose_name
        ordering = ['id']


# 出版社表
class tpress(models.Model):
    p_id = models.CharField(max_length=200, verbose_name="出版社id", null=True, blank=True)
    p_name = models.CharField(max_length=200, verbose_name="出版社名称", null=True, blank=True)
    p_src = models.CharField(max_length=200, verbose_name="出版社链接", null=True, blank=True)

    def __str__(self):
        return self.p_name

    class Meta:
        pass
        # verbose_name = '出版社'
        # verbose_name_plural = verbose_name


# 学科信息表
# class tclass(models.Model):
#     id = models.CharField(max_length=200, verbose_name="学科分类id", blank=True,primary_key=True)
#     c_name = models.CharField(max_length=200, verbose_name="学科名称", null=True, blank=True)
#     c_src = models.CharField(max_length=200, verbose_name="学科链接", null=True, blank=True)
#
#     def __str__(self):
#         return self.c_name
#
#     class Meta:
#         verbose_name = '学科分类'
#         verbose_name_plural = verbose_name
