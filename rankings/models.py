#-*- coding: utf-8 -*-
import os
import sys

CURRENT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
BACKEND_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
APP_DIR = os.path.abspath(os.path.join(BACKEND_DIR, os.pardir))
WEBAPPS_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

sys.path.insert(0, BACKEND_DIR + '/')
sys.path.insert(0, APP_DIR + '/')
sys.path.insert(0, WEBAPPS_DIR + '/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python_core.settings'

print CURRENT_DIR
print BACKEND_DIR
print APP_DIR
print WEBAPPS_DIR

from django.db import models

# Create your models here.

"""
Each row is a race, with its general information. (Where, category, etc...)
"""


class Races(models.Model):
    info = models.TextField(max_length=255)
    category = models.TextField(max_length=255)
    genre = models.TextField(max_length=255)
    link = models.TextField(max_length=511)
    location = models.TextField(max_length=255)
    discipline = models.TextField(max_length=255)
    raceId = models.IntegerField()
    table = models.TextField()
    date = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.info
