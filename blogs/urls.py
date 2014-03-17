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
    regex=r'^bloggers/$',
    view='bloggers',
    name='basic_urls',
    ),

    url(
    regex=r'^posts/$',
    view='posts',
    name='basic_urls',
    ),

    url(
    regex=r'^bloggers/save/$',
    view='saveBlogger',
    name='basic_urls',
    ),

    url(
    regex=r'^posts/save/$',
    view='savePost',
    name='basic_urls',
    ),

    url(
    regex=r'^bloggers/delete/$',
    view='deleteBlogger',
    name='basic_urls',
    ),

    url(
    regex=r'^posts/delete/$',
    view='deletePost',
    name='basic_urls',
    ),

)
