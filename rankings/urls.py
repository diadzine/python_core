#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from rankings import views

urlpatterns = patterns(
    'rankings.views',
    url(
        regex=r'^$',
        view='get',
        name='basic_urls',
    ),

    url(
        regex=r'^rankings/$',
        view='get',
        name='basic_urls',
    ),

    url(
        regex=r'^save/$',
        view='save',
        name='basic_urls',
    ),

)
