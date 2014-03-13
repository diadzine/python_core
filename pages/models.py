#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Pages(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(null=True)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.name