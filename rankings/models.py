#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

"""
Each row is a race, with its general information. (Where, category, etc...)
"""


class Races(models.Model):
    email = models.TextField(max_length=255)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.name

"""
Each entry is a line of a race's result. It includes the information given
form the FIS ski website.
"""


class Results(models.Model):
    email = models.TextField(max_length=255)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.name

"""
Each row is a row of the general ranking of the FIS.
"""


class Leaders(models.Model):
    place = models.PositiveSmallIntegerField()
    name = models.TextField(max_length=255)
    country = models.TextField(max_length=255)
    gender = models.TextField(max_length=20)
    points = models.PositiveSmallIntegerField()
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.name
