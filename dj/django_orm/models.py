#coding=utf-8
from django.db import models
class checkcode(models.Model):
    code=models.CharField(max_length=255)
    create_date=models.DateTimeField()
    mobile=models.CharField(max_length=255)
    enable_flag=models.BooleanField(default=False)
    _id=models.CharField(max_length=255,db_index=True,unique=True)
    type=models.CharField(max_length=255)
