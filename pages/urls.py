from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns(
    'pages.views',
    url(
    regex=r'^$',
    view='get',
    name='basic_urls',
    ),

    url(
        regex=r'^get$',
        view='get',
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
