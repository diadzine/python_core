#-*- coding: utf-8 -*-
import os
import sys
CURRENT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
SPIDERS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
SCRAPY_DIR = os.path.abspath(os.path.join(SPIDERS_DIR, os.pardir))
MODULE_DIR = os.path.abspath(os.path.join(SCRAPY_DIR, os.pardir))
BACKEND_DIR = os.path.abspath(os.path.join(MODULE_DIR, os.pardir))
APP_DIR = os.path.abspath(os.path.join(BACKEND_DIR, os.pardir))
WEBAPPS_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

sys.path.append(BACKEND_DIR + '/')
sys.path.append(APP_DIR + '/')
sys.path.append(MODULE_DIR + '/')
sys.path.append(WEBAPPS_DIR + '/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python_core.settings'

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
