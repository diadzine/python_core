#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Bloggers(models.Model):
        # Note: Ad and sponsors contains many addresses which are separated by
        # |.
    name = models.CharField(max_length=510)
    biography = models.TextField(null=True)
    linkResults = models.TextField(null=True)
    profilePic = models.TextField(null=True)
    sponsors = models.TextField(null=True)
    ad = models.TextField(null=True)
    header = models.TextField(null=True)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.name


class BlogPosts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    blogId = models.SmallIntegerField(null=True)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.title
