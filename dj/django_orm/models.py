#coding=utf-8
from django.db import models
class checkcode(models.Model):
    _id = models.CharField(max_length=255,db_index=True,unique=True)
    blog_href = models.CharField(max_length=255)
    blog_name = models.CharField(max_length=255)
