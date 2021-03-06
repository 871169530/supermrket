from django.core import validators
from django.db import models

# Create your models here.
from db.base_model import BaseModel


class Users(BaseModel):
    sex_choices = (
        (1, '男'),
        (2, "女"),
        (3, "保密"),
    )
    nickname = models.CharField(verbose_name='昵称',
                                max_length=20,
                                null=True,
                                blank=True,
                                )
    phone = models.CharField(verbose_name='手机号码',
                             max_length=12,
                             validators=[
                                 validators.RegexValidator(r'^1[3-9]\d{9}$','手机号码格式错误！')
                             ])
    password = models.CharField(verbose_name='密码',
                                max_length=64,
                                )
    gender = models.SmallIntegerField(verbose_name='性别',
                                      default=3,
                                      choices=sex_choices,
                                      )
    head = models.ImageField(verbose_name='用户头像',
                             upload_to='head/%Y/%m',
                             default='user/201809/25/B.jpg'
                             )

    birthday = models.DateField(verbose_name='出生日期',
                                null=True,
                                blank=True,
                                )
    school_name = models.CharField(verbose_name='学校名称',
                                   max_length=50,
                                   null=True,
                                   blank=True,
                                   )
    address = models.CharField(verbose_name='学校详细地址',
                               max_length=100,
                               null=True,
                               blank=True,
                               )
    hometown = models.CharField(verbose_name='老家',
                                max_length=100,
                                null=True, blank=True,
                                )

    class Meta:
        verbose_name = '管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.phone


class TestImageModel(models.Model):
    head = models.ImageField(upload_to='user/%Y%m/%d',verbose_name='用户头像')