#coding=utf-8

from django.conf import settings
from django.core.management import call_command

def models_py_import():
            models_py_import_str = "#coding=utf-8\n"
            models_py_import_str += "\n"
            models_py_import_str += "from django.db import models\n"
            models_py_import_str += "\n"
            return models_py_import_str

def write_models_py(models_py_import_str,class_str_list):
    f = open(settings.BASE_DIR + "/django_orm/models.py","w")
    f.write(models_py_import_str)
    for class_str in class_str_list:
        f.write(class_str)
        f.write("\n")
    f.close()

def auto_rebuild_table(connections,table_names):
    db = "default"
    connection = connections[db]
    cursor = connection.cursor()
    try :
        for table_name in table_names:
            cursor.execute("drop table django_orm_%s;"%table_name.lower())
    except  Exception,e:
        print str(e)
        pass

    call_command("validate")
    call_command("syncdb")