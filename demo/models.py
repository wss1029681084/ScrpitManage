#!/usr/bin/python3
# -*- coding:utf-8 -*-
from django.db import models
from .utils import gethostname

# Create your models here.
##


class  Server(models.Model):
    server_name=models.CharField(max_length=50, verbose_name='名称')
    hostname=models.CharField(max_length=50, verbose_name='IP')
    username = models.CharField(max_length=50, verbose_name='账号')
    passwd = models.CharField(max_length=50, verbose_name='密码')
    port = models.CharField(max_length=50, verbose_name='端口')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    class Meta:
       db_table = 'Server'
       verbose_name_plural ="服务器用户"

    def __str__(self):
       return self.server_name
class Publish(models.Model):
    choices = (
        ('CodePublish', '代码部署'),
        ('RunScrpit', '执行脚本'),
        ('Monitor','服务监控')
    )
    Publish_name = models.CharField(max_length=50,verbose_name='发布项目')
    host=models.ForeignKey('Server',on_delete=models.CASCADE,)
    script= models.CharField(max_length=500,verbose_name='脚本')
    param=models.CharField(max_length=500,verbose_name='参数')
    update_time = models.DateTimeField(auto_now=True)
    type=models.CharField(verbose_name='发布类型',choices=choices,max_length=50,)

    class Meta:
        verbose_name = '发布脚本'
        verbose_name_plural = '发布'

    def __str__(self):
        return self.Publish_name
# class Function(models.Model):
#     class Meta:
#         verbose_name = u"自定义"
#         verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.Meta.verbose_name
