#coding=utf-8

import pdb
import pymongo
import datetime
import bson

class BaseField(object):

    def __init__(self,column_name,column_type):
        self.column_name = column_name
        self.column_type = column_type

    def model_field(self,column_name,field_type,field_desc):
        model_field_line = "    %s = models.%s(%s)\n"%(column_name,field_type,field_desc)
        return model_field_line

    def process(self,*args,**kwargs):
        column_name, field_type, field_desc = self.parse(*args,**kwargs)
        model_field_line = self.model_field(column_name,field_type,field_desc)
        return model_field_line

class StrField(BaseField):

    field_type = str(str)

    def parse(self,*args,**kwargs):
        if self.column_type !=  StrField.field_type:
            raise Exception("column type error : must be %s"%StrField.field_type)
        else:
            field_type = "CharField"
            field_desc = "max_length=255"
        return self.column_name, field_type, field_desc

class UnicodeField(BaseField):

    field_type = str(type(u"str"))

    def parse(self,*args,**kwargs):
        if self.column_type != UnicodeField.field_type :
            raise Exception("column type error : must be %s"%UnicodeField.field_type)
        else:
            field_type = "CharField"
            field_desc = "max_length=255"
        return self.column_name, field_type, field_desc

class BooleanField(BaseField):

    field_type = str(bool)

    def parse(self,*args,**kwargs):
        if self.column_type !=  BooleanField.field_type:
            raise Exception("column type error : must be %s"%BooleanField.field_type)
        else:
            field_type = "BooleanField"
            field_desc = "default=False"
        return self.column_name, field_type, field_desc

class IntegerField(BaseField):

    field_type = str(int)

    def parse(self,*args,**kwargs):
        if self.column_type !=  IntegerField.field_type:
            raise Exception("column type error : must be %s"%IntegerField.field_type)
        else:
            field_type = "IntegerField"
            field_desc = ""
        return self.column_name, field_type, field_desc

class FloatField(BaseField):

    field_type = str(float)

    def parse(self,*args,**kwargs):
        if self.column_type !=  FloatField.field_type:
            raise Exception("column type error : must be %s"%FloatField.field_type)
        else:
            field_type = "FloatField"
            field_desc = ""
        return self.column_name, field_type, field_desc

class NoneField(BaseField):

    field_type = str(type(None))

    def parse(self,*args,**kwargs):
        if self.column_type !=  NoneField.field_type:
            raise Exception("column type error : must be %s"%NoneField.field_type)
        else:
            field_type = "CharField"
            field_desc = "max_length=255"
        return self.column_name, field_type, field_desc

class ListField(BaseField):

    field_type =  str(list)

    def parse(self,*args,**kwargs):
        if self.column_type !=  ListField.field_type:
            raise Exception("column type error : must be %s"%ListField.field_type)
        else:
            field_type = "TextField"
            field_desc = ""
        return self.column_name, field_type, field_desc

class DictField(BaseField):

    field_type = str(dict)

    def parse(self,*args,**kwargs):
        if self.column_type !=  DictField.field_type:
            raise Exception("column type error : must be %s"%DictField.field_type)
        else:
            field_type = "TextField"
            field_desc = ""
        return self.column_name, field_type, field_desc

class ObjectIdField(BaseField):

    field_type = str(bson.objectid.ObjectId)

    def parse(self,*args,**kwargs):
        if self.column_type !=  ObjectIdField.field_type:
            raise Exception("column type error : must be %s"%ObjectIdField.field_type)
        else:
            field_type = "CharField"
            field_desc = "max_length=255,db_index=True,unique=True"
        return self.column_name, field_type, field_desc

class DateTimeField(BaseField):

    field_type = str(datetime.datetime)

    def parse(self,*args,**kwargs):
        if self.column_type !=  DateTimeField.field_type:
            raise Exception("column type error : must be %s"%DateTimeField.field_type)
        else:
            field_type = "DateTimeField"
            field_desc = ""
        return self.column_name, field_type, field_desc

class RegexField(BaseField):

    field_type = str(bson.regex.Regex)

    def parse(self,*args,**kwargs):
        if self.column_type !=  RegexField.field_type:
            raise Exception("column type error : must be %s"%RegexField.field_type)
        else:
            field_type = "DateTimeField"
            field_desc = ""
        return self.column_name, field_type, field_desc

type_field_mapping = {
            str(str):StrField,
            str(type(u"str")):UnicodeField,
            str(bool):BooleanField,
            str(int):IntegerField,
            str(float):FloatField,
            str(type(None)):NoneField,
            str(list): ListField,
            str(dict):DictField,
            str(bson.objectid.ObjectId):ObjectIdField,
            str(datetime.datetime):DateTimeField,
            str(bson.regex.Regex):RegexField,
        }

class Many2ManyField(BaseField):
    field_type = str(list)

    def parse(self, *args, **kwargs):
        table_name = args[0]
        if self.column_type != ListField.field_type:
            raise Exception("column type error : must be %s" % ListField.field_type)
        else:
            field_type = "ManyToManyField"
            field_desc = table_name
        return self.column_name, field_type, field_desc

class ForeignKeyField(BaseField):
    field_type = str(dict)

    def parse(self, *args, **kwargs):
        table_name = args[0]
        if self.column_type != DictField.field_type:
            raise Exception("column type error : must be %s" % DictField.field_type)
        else:
            field_type = "ForeignKey"
            field_desc = table_name
        return self.column_name, field_type, field_desc

relation_type_field_mapping = {
    str(list): Many2ManyField,
    str(dict): ForeignKeyField,
}
