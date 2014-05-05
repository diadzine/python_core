#-*- coding: utf-8 -*-
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
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.name
