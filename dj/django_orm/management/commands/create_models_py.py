#coding=utf-8
from optparse import make_option
import itertools
import traceback
import pdb

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.management.color import no_style
from django.core.management.sql import custom_sql_for_model, emit_post_sync_signal, emit_pre_sync_signal
from django.db import connections, router, transaction, models, DEFAULT_DB_ALIAS
from django.utils.datastructures import SortedDict
from django.utils.importlib import import_module
import pymongo
import datetime
import bson

from django_orm import fields

# {
#     "String":"niyoufa",
#     "Integer":10,
#     "Boolean":false,
#     "Float":10.0,
#     "Double":10.0,
#     "Date":new Date(),
#     "ObjectId":ObjectId("578d8b2ae20286d3ebea738d"),
#     "Null":null,
#     "Object":{"name":"niyoufa"},
#     "RegExp":RegExp("/[a-z]"),
#     "Number":Number(10)
# }
# {"String":"niyoufa","Integer":10,"Boolean":false,"Float":10.0,"Double":10.0,"Date":new Date(),"ObjectId":ObjectId("578d8b2ae20286d3ebea738d"),"Null":null,"Object":{"name":"niyoufa"},"RegExp":RegExp("/[a-z]"),"Number":Number(10)}

class Command(BaseCommand):

    def handle(self, **options):

        def models_py_import():
            models_py_import_str = "#coding=utf-8\n"
            models_py_import_str += "\n"
            models_py_import_str += "from django.db import models\n"
            models_py_import_str += "\n"
            return models_py_import_str

        def models_py_class(table_name):
            models_py_class_str = "class %s(models.Model):\n"%table_name
            return models_py_class_str

        def write_models_py(class_str):
            f = open(settings.BASE_DIR + "/django_orm/models.py","w")
            f.write(class_str)
            f.close()

        client = pymongo.MongoClient("localhost", 27017)
        db = client["code"]
        coll = db["order"]
        table_name = coll.name
        obj = coll.find_one()
        columns = []
        for column in obj.keys():
            columns.append((column,str(type(obj[column]))))
        print "start create models.py"
        models_py_import_str = models_py_import()
        models_py_class_str = models_py_class(table_name)
        column_list_str = ""
        for column in columns:
            column_name = column[0]
            field_type = column[1]
            column_list_str += fields.type_field_mapping[field_type](column_name,field_type).process()

        class_str = models_py_import_str + models_py_class_str + column_list_str
        write_models_py(class_str)

        db = "default"
        connection = connections[db]
        cursor = connection.cursor()
        try :
            cursor.execute("drop table django_orm_%s;"%table_name)
        except  Exception,e:
            print str(e)
            pass

        call_command("validate")
        call_command("syncdb")