#coding=utf-8

from django.db import models

class image(models.Model):
    upload_key = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)
    file_memo = models.CharField(max_length=255)
    file_hash = models.CharField(max_length=255)
    file_ctms = models.FloatField()
    file_mark = models.CharField(max_length=255)
    _id = models.CharField(max_length=255,db_index=True,unique=True)
    file_path = models.CharField(max_length=255)

class auth(models.Model):
    status = models.TextField()
    front_photo = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    uid = models.CharField(max_length=255)
    audit_date = models.DateTimeField()
    hand_photo = models.CharField(max_length=255)
    edit_status = models.TextField()
    id_card = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    promise_photo = models.CharField(max_length=255)
    auditor = models.CharField(max_length=255)
    _id = models.CharField(max_length=255,db_index=True,unique=True)
    type = models.TextField()
    back_photo = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class user(models.Model):
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    invitation_mobile = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    login_date = models.DateTimeField()
    comment = models.CharField(max_length=255)
    sex = models.IntegerField()
    username = models.CharField(max_length=255)
    active = models.IntegerField()
    admin_password = models.CharField(max_length=255)
    write_date = models.CharField(max_length=255)
    contact_mobile = models.CharField(max_length=255)
    privilege = models.IntegerField()
    headimgurl = models.CharField(max_length=255)
    _id = models.CharField(max_length=255,db_index=True,unique=True)
    type = models.TextField()
    email = models.CharField(max_length=255)

class oauth_clients(models.Model):
    redirect_uris = models.TextField()
    secret = models.CharField(max_length=255)
    _id = models.CharField(max_length=255,db_index=True,unique=True)
    authorized_grants = models.TextField()
    identifier = models.CharField(max_length=255)

