from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    #手机号
    mobile = models.CharField(max_length=11, unique=True, blank=False)
    #头像信息
    avatar = models.ImageField(upload_to='avatar/%Y%m%d',blank=True)
    #简介
    users_desc = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = 'tb_users'#修改表名
        verbose_name = '用户管理'#adein 后台显示
        verbose_name_plural = verbose_name #adein 后台显示

    def __str__(self):
        return self.mobile

