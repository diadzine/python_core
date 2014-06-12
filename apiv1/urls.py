# from django.conf.urls import (
#     patterns,
#     url,
#     include,
# )

# from rest_framework.authtoken.views import obtain_auth_token

# import apiv1.views
# import users.views
# import company.views

# urlpatterns = patterns(
#     'apiv1.views',

#     url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

#     url(r'^auth-token/', obtain_auth_token),

#     url(regex=r'^users/is_admin/$',
#         view=users.views.is_admin,
#         name='Custom View'),

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

#     url(regex=r'^agent_types/$',
#         view=apiv1.views.AgentTypeCreateReadView.as_view(),
#         name='REST View'),

#     url(regex=r'^agent_types/(?P<pk>[-\w]+)/$',
#         view=apiv1.views.AgentTypeReadUpdateDeleteView.as_view(),
#         name='REST View'),

#     url(regex=r'^agents/$',
#         view=apiv1.views.AgentCreateReadView.as_view(),
#         name='REST View'),

#     url(regex=r'^agents/tree/$',
#         view=company.views.agents_tree,
#         name='REST View'),

#     url(regex=r'^agents/(?P<pk>[-\w]+)/$',
#         view=apiv1.views.AgentReadUpdateDeleteView.as_view(),
#         name='REST View'),

#     url(regex=r'^transactions/$',
#         view=apiv1.views.TransactionCreateReadView.as_view(),
#         name='REST View'),

#     url(regex=r'^transactions/(?P<pk>[-\w]+)/$',
#         view=apiv1.views.TransactionReadUpdateDeleteView.as_view(),
#         name='REST View'),

#     url(regex=r'^product_families/$',
#         view=apiv1.views.ProductFamilyCreateReadView.as_view(),
#         name='REST View'),

#     url(regex=r'^product_families/(?P<pk>[-\w]+)/$',
#         view=apiv1.views.ProductFamilyReadUpdateDeleteView.as_view(),
#         name='REST View'),

#     url(regex=r'^currencies/$',
#         view=apiv1.views.CurrencyCreateReadView.as_view(),
#         name='REST View'),

#     url(regex=r'^currencies/(?P<pk>[-\w]+)/$',
#         view=apiv1.views.CurrencyReadUpdateDeleteView.as_view(),
#         name='REST View'),

#     url(regex=r'^exchange_rates/$',
#         view=apiv1.views.ExchangeRateCreateReadView.as_view(),
#         name='REST View'),

#     url(regex=r'^exchange_rates/(?P<pk>[-\w]+)/$',
#         view=apiv1.views.ExchangeRateReadUpdateDeleteView.as_view(),
#         name='REST View'),
# )
