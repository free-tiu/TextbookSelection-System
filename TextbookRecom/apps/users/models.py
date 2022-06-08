from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    # phone = models.CharField(max_length=11, verbose_name="用户电话", null=True, blank=True)
    college = models.CharField(max_length=200, verbose_name="用户所属学院", null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name