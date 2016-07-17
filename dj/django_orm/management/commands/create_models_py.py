from optparse import make_option
import itertools
import traceback

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.management.color import no_style
from django.core.management.sql import custom_sql_for_model, emit_post_sync_signal, emit_pre_sync_signal
from django.db import connections, router, transaction, models, DEFAULT_DB_ALIAS
from django.utils.datastructures import SortedDict
from django.utils.importlib import import_module


class Command(BaseCommand):

    def handle(self, **options):
        print "start create models.py"

        f = open(settings.BASE_DIR + "/django_orm/models.py","w")
        f.write("#coding=utf-8\n")
        f.write("from django.db import models\n")
        f.write("class blog(models.Model):\n")
        f.write("    _id = models.CharField(max_length=255,db_index=True,unique=True)\n")
        f.write("    blog_href = models.CharField(max_length=255)\n")
        f.write("    blog_name = models.CharField(max_length=255)\n")

        f.close()

        db = "default"
        connection = connections[db]
        cursor = connection.cursor()
        try :
            cursor.execute("drop table django_orm_blog;")
        except  Exception,e:
            print str(e)
            pass

        call_command("validate")
        call_command("syncdb")
