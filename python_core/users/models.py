#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Users(models.Model):
    email = models.TextField(max_length=255)
    password = models.TextField(null=True)
    name = models.TextField(null=True)
    signature = models.TextField(null=True)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.name