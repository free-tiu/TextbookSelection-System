from django.db import models

# Create your models here.
from users.models import Users


class Collection(models.Model):
    c_name = models.ForeignKey(Users, verbose_name="收藏用户", on_delete=models.CASCADE)
    c_id = models.IntegerField(verbose_name="收藏id")
    c_status = models.BooleanField(default=False, verbose_name="收藏状态")

    def __str__(self):
        return self.c_name.username

    class Meta:
        verbose_name = '收藏信息管理'
        verbose_name_plural = verbose_name