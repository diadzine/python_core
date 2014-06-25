from django.conf.urls import patterns, url

from skiclubs import views

urlpatterns = patterns(
    'skiclubs.views',
    url(
        regex=r'^$',
        view='upload',
        name='basic_urls',
    ),

)
