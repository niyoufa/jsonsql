#coding=utf-8

from django.db import models

class List(models.Model):
    name = models.CharField(max_length=255)

class Dict(models.Model):
    name = models.CharField(max_length=255)

class order(models.Model):
    String = models.CharField(max_length=255)
    Double = models.FloatField()
    Float = models.FloatField()
    Boolean = models.BooleanField(default=False)
    Integer = models.FloatField()
    _id = models.CharField(max_length=255,db_index=True,unique=True)

