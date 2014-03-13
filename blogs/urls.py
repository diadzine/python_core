from django.conf.urls import patterns, url

from blogs import views

urlpatterns = patterns(
    'blogs.views',
    url(
    regex=r'^$',
    view='bloggers',
    name='basic_urls',
    ),

    url(
    regex=r'^bloggers$',
    view='bloggers',
    name='basic_urls',
    ),

    url(
    regex=r'^posts$',
    view='posts',
    name='basic_urls',
    ),

)
