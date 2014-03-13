#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    author = models.TextField(null=True)
    content = models.TextField(null=True)
    mag = models.SmallIntegerField(null=True)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.title

class Posts(models.Model):
    title = models.CharField(max_length=255)
    author = models.TextField(null=True)
    content = models.TextField(null=True)
    mag = models.SmallIntegerField(null=True)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.title