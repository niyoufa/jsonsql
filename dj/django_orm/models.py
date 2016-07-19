#coding=utf-8

from django.db import models

class order(models.Model):
    Null = models.CharField(max_length=255)
    String = models.CharField(max_length=255)
    ObjectId = models.CharField(max_length=255,db_index=True,unique=True)
    Double = models.FloatField()
    Float = models.FloatField()
    Number = models.FloatField()
    Object = models.TextField()
    Boolean = models.BooleanField(default=False)
    RegExp = models.DateTimeField()
    Date = models.DateTimeField()
    Integer = models.FloatField()
    _id = models.CharField(max_length=255,db_index=True,unique=True)
