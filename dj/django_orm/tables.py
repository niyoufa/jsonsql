#coding=utf-8

import pdb
from django_orm import fields
from django_orm import utils

class ModelClass(object):

        def __init__(self,table_name,coll):
            self.table_name = table_name
            self.coll = coll
            self.class_str = ""
            self.table_name_list = [table_name]

        def parse(self,*args,**options):
            models_py_class_str = self.models_py_class(self.table_name)
            models_py_column_list_str , class_str_list  = self.models_py_field(self.coll,fields)
            class_str_list.extend([models_py_class_str + models_py_column_list_str])
            self.class_str_list = class_str_list
            return class_str_list

        def models_py_field(self,coll,fields):
            obj = coll.find_one()
            columns = []
            class_columns = []

            for column in obj.keys():
                if type(obj[column]) == dict or \
                ( type(obj[column]) == list and len(obj[column][0])>0 and type(obj[column][0]) == dict ):
                    class_columns.append((column,str(type(obj[column]))))
                columns.append((column,str(type(obj[column]))))
            column_list_str = ""
            for column in columns:
                column_name = column[0]
                field_type = column[1]
                column_list_str += fields.type_field_mapping[field_type](column_name,field_type).process(column_name)

            class_str_list = []
            for class_column in class_columns:
                column_name = class_column[0]
                field_type = class_column[1]
                class_str = self.prase_sub_class_str(column_name,field_type,obj[column_name])
                class_str_list.append(class_str)

            return column_list_str , class_str_list

        def models_py_class(self,table_name):
            models_py_class_str = "class %s(models.Model):\n"%table_name
            return models_py_class_str

        def prase_sub_class_str(self,table_name,field_type,obj):
            models_py_class_str = self.models_py_class(table_name)
            if field_type == str(dict):
                models_py_column_list_str = self.sub_models_py_field(obj)
            elif field_type == str(list):
                models_py_column_list_str = self.sub_models_py_field(obj[0])
            class_str = models_py_class_str + models_py_column_list_str
            self.table_name_list.append(table_name)
            return class_str

        def sub_models_py_field(self,obj):
            columns = []
            for column in obj.keys():
                columns.append((column,str(type(obj[column]))))
            column_list_str = ""
            for column in columns:
                column_name = column[0]
                field_type = column[1]
                column_list_str += fields.type_field_mapping[field_type](column_name,field_type).process()
            return column_list_str