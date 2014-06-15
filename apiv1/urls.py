from django.conf.urls import (
    patterns,
    url,
    include,
)

from rest_framework.authtoken.views import obtain_auth_token

import apiv1.views

# urlpatterns = patterns(
#     'apiv1.views',

#     url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

#     url(r'^auth-token/', obtain_auth_token),

#     url(regex=r'^users/$',
#         view=apiv1.views.UserCreateReadView.as_view(),
#         name='REST View'),

#     url(regex=r'^users/agents/$',
#         view=apiv1.views.AgentsForUserCreateReadView.as_view(),
#         name='REST View'),

#     url(regex=r'^users/(?P<pk>[-\w]+)/$',
#         view=apiv1.views.UserReadUpdateDeleteView.as_view(),
#         name='REST View'),

#     url(regex=r'^users/(?P<pk>[-\w]+)/set_password/$',
#         view=users.views.set_password,
#         name='Custom View'),
# )