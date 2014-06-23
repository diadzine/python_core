from django.conf.urls import patterns, url

from pictures import views

urlpatterns = patterns(
    'pictures.views',
    url(
        regex=r'^$',
        view='upload',
        name='basic_urls',
    ),

)
