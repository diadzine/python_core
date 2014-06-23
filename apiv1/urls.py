from django.conf.urls import (
    patterns,
    url,
    include,
)

from rest_framework.authtoken.views import obtain_auth_token

import apiv1.views

urlpatterns = patterns(
    'apiv1.views',

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^auth-token/', obtain_auth_token),

    url(regex=r'^news/$',
        view=apiv1.views.NewsCreateReadView.as_view(),
        name='REST View'),

    url(regex=r'^news/(?P<pk>[-\w]+)/$',
        view=apiv1.views.NewsReadUpdateDeleteView.as_view(),
        name='REST View'),

    url(regex=r'^ads/$',
        view=apiv1.views.AdsCreateReadView.as_view(),
        name='REST View'),

    # url(regex=r'^ads/horizontal/$',
    #     view=apiv1.views.AdsCreateReadView.as_view(),
    #     name='REST View'),

    # url(regex=r'^ads/vertical/$',
    #     view=apiv1.views.AdsCreateReadView.as_view(),
    #     name='REST View'),

    # url(regex=r'^ads/square/$',
    #     view=apiv1.views.AdsCreateReadView.as_view(),
    #     name='REST View'),

    url(regex=r'^ads/(?P<pk>[-\w]+)/$',
        view=apiv1.views.AdsReadUpdateDeleteView.as_view(),
        name='REST View'),
)
