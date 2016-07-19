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

# {
#     "String":"niyoufa",
#     "Integer":10,
#     "Boolean":false,
#     "Double":10.0,
#     "Date":new Date(),
#     "ObjectId":ObjectId("578d8b2ae20286d3ebea738d"),
#     "Null":null,
#     "Object":{"name":"niyoufa"},
#     "RegExp":RegExp("/[a-z]"),
#     "Number":Number(10)
# }

class Command(BaseCommand):

    def handle(self, **options):

        client = pymongo.MongoClient("localhost", 27017)
        db = client["dhui100"]
        coll = db["order"]
        table_name = coll.name
        obj = coll.find_one()
        columns = []
        for column in obj.keys():
            columns.append((column,str(type(obj[column]))))

        type_mapping = {
            str(str):'models.CharField(max_length=255)',
            str(type(u"str")):'models.CharField(max_length=255)',
            str(datetime.datetime):'models.DateTimeField()',
            str(bool):'models.BooleanField(default=False)',
            str(bson.objectid.ObjectId):'models.CharField(max_length=255,db_index=True,unique=True)',
            str(type(None)):'models.CharField(max_length=255)',
            str(float):'models.FloatField()',
            str(list): 'models.TextField()',
            str(dict):'models.TextField()',
            str(bson.regex.Regex):'models.TextField()',
            str(int):'models.IntegerField()',
        }

        print "start create models.py"

        f = open(settings.BASE_DIR + "/django_orm/models.py","w")
        f.write("#coding=utf-8\n")
        f.write("from django.db import models\n")
        f.write("class %s(models.Model):\n"%table_name)
        for column in columns:
            f.write('    %s=%s\n' % (column[0], type_mapping[column[1]]))
        f.close()

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
