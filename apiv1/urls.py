from django.conf.urls import (
    patterns,
    url,
    include,
)

from rest_framework.authtoken.views import obtain_auth_token

import apiv1.views
import news.views
import rankings.views
import blogs.views

urlpatterns = patterns(
    'apiv1.views',

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^auth-token/', obtain_auth_token),

    url(regex=r'^news/$',
        view=apiv1.views.NewsCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^news/rss/$',
        view=news.views.RSSFeed(),
        name='REST View'),

    url(regex=r'^mag/$',
        view=apiv1.views.MagCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^news/(?P<pk>[-\w]+)/$',
        view=apiv1.views.NewsReadUpdateDeleteView.as_view(),
        name='REST View'),

    url(regex=r'^news_admin/$',
        view=apiv1.views.NewsAdminCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^news_admin/(?P<pk>[-\w]+)/$',
        view=apiv1.views.NewsAdminReadUpdateDeleteView.as_view(),
        name='REST View'),

    url(regex=r'^ads/$',
        view=apiv1.views.AdsCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^ads/placeholders/$',
        view=apiv1.views.AdsPlaceholdersReadView.as_view(),
        name='REST View'),

    url(regex=r'^ads/(?P<pk>[-\w]+)/$',
        view=apiv1.views.AdsReadUpdateDeleteView.as_view(),
        name='REST View'),

    url(regex=r'^bloggers/$',
        view=apiv1.views.BloggersCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^bloggers/rss/$',
        view=blogs.views.BlogsRSS(),
        name='REST View'),

    url(regex=r'^bloggers/(?P<pk>[-\w]+)/$',
        view=apiv1.views.BloggersReadUpdateDeleteView.as_view(),
        name='REST View'),

    url(regex=r'^bloggers/(?P<blogger>[-\w]+)/posts/$',
        view=apiv1.views.BlogPostsCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^bloggers/(?P<blogger>[-\w]+)/posts/(?P<pk>[-\w]+)/$',
        view=apiv1.views.BlogPostsReadUpdateDeleteView.as_view(),
        name='REST View'),

    url(regex=r'^skiclubs/$',
        view=apiv1.views.SkiclubsCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^skiclubs/(?P<pk>[-\w]+)/$',
        view=apiv1.views.SkiclubsReadUpdateDeleteView.as_view(),
        name='REST View'),

    url(regex=r'^pages/$',
        view=apiv1.views.PagesCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^pages/(?P<pk>[-\w]+)/$',
        view=apiv1.views.PagesReadUpdateDeleteView.as_view(),
        name='REST View'),

    url(regex=r'^widgets/$',
        view=apiv1.views.WidgetsCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^widgets/(?P<pk>[-\w]+)/$',
        view=apiv1.views.WidgetsReadUpdateDeleteView.as_view(),
        name='REST View'),

    url(regex=r'^races/$',
        view=rankings.views.last_races,
        name='REST View'),

    url(regex=r'^races/update/$',
        view=rankings.views.update,
        name='REST View'),

    url(regex=r'^races/(?P<pk>[-\w]+)/$',
        view=rankings.views.race,
        name='REST View'),

    url(regex=r'^races/cat/(?P<category>.+)/$',
        view=rankings.views.race_category,
        name='REST View'),

    # url(regex=r'^races/$',
    #     view=apiv1.views.RacesCreateReadView.as_view(),
    #     name='REST View'),

    # url(regex=r'^races/(?P<pk>[-\w]+)/$',
    #     view=apiv1.views.RacesReadUpdateDeleteView.as_view(),
    #     name='REST View'),

    # url(regex=r'^races/cat/(?P<category>.+)/$',
    #     view=apiv1.views.RacesCategoryCreateReadView.as_view(),
    #     name='REST View'),

    url(regex=r'^angulation/covers/$',
        view=apiv1.views.CoversCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^angulation/covers/(?P<pk>[-\w]+)/$',
        view=apiv1.views.CoversReadUpdateDeleteView.as_view(),
        name='REST View'),
)
