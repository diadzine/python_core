from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns(
    'users.views',
    url(
    regex=r'^$',
    view='login',
    name='basic_urls',
    ),

    url(
        regex=r'^login$',
        view='login',
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
