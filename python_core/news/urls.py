from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns(
    'news.views',
    url(
    regex=r'^$',
    view='home',
    name='basic_urls',
    ),

    url(
    regex=r'^get$',
    view='home',
    name='basic_urls',
    ),

    url(
    regex=r'^save$',
    view='save',
    name='basic_urls',
    ),

    url(
    regex=r'^delete$',
    view='delete',
    name='basic_urls',
    ),

)
