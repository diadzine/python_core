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
        regex=r'^latest$',
        view='latest_entries',
        name='basic_urls'
    ),

)
