from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'PersHo.views.home', name='home'),
    # url(r'^PersHo/', include('PersHo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(
        r'^news/',
        include('news.urls')
    ),

    url(
        r'^users/',
        include('users.urls')
    ),

    url(
        r'^pages/',
        include('pages.urls')
    ),

    url(
        r'^blogs/',
        include('blogs.urls')
    ),

    url(
        r'^ads/',
        include('ads.urls')
    ),

    url(
        r'^rankings/',
        include('rankings.urls')
    ),

    url(
        r'^apiv1/',
        include('apiv1.urls')
    ),
)
