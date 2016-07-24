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

from django_orm import tables
from django_orm import utils

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
#     "List":[{"name":"niyoufa"}]
#     "Dict":{"name":"niyoufa"}
# }
# {"String":"niyoufa","Integer":10,"Boolean":false,"Float":10.0,"Double":10.0,"Date":new Date(),"ObjectId":ObjectId("578d8b2ae20286d3ebea738d"),"Null":null,"Object":{"name":"niyoufa"},"RegExp":RegExp("/[a-z]"),"Number":Number(10)}

class Command(BaseCommand):

    def handle(self, **options):

        print "start create models.py"
        models_py_import_str = utils.models_py_import()

        client = pymongo.MongoClient("localhost", 27017)
        db = client["code"]

        db_class_str_list = []

        coll = db["order"]
        table_name = coll.name
        model_class_obj = tables.ModelClass(table_name,coll)
        class_str_list = model_class_obj.parse()
        db_class_str_list.extend(class_str_list)

        # write models.py
        utils.write_models_py(models_py_import_str,db_class_str_list)
        # rebuild table
        utils.auto_rebuild_table(connections,model_class_obj.table_name_list)