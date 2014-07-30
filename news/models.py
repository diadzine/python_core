#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.TextField(null=True)
    content = models.TextField(null=True)
    mag = models.SmallIntegerField(null=True)
    date = models.DateTimeField(
        auto_now_add=False,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.title


class OldNews(models.Model):
    Titre = models.TextField(null=True)
    Date = models.TextField(null=True)
    Texte = models.TextField(null=True)
    Auteur = models.TextField(null=True)
    Analyse = models.BooleanField()
    Resultats = models.BooleanField()
    Interview = models.BooleanField()

    def __unicode__(self):
        return u'%s' % self.Titre
