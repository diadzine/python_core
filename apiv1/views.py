# from rest_framework.generics import (
#     ListAPIView,
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
# from rest_framework.permissions import (
#     IsAuthenticated,
#     IsAdminUser,
# )

# from apiv1.serializers import (
#     UserSerializer,
#     AgentTypeSerializer,
#     AgentSerializer,
#     TransactionSerializer,
#     ProductFamilySerializer,
#     CurrencySerializer,
#     ExchangeRateSerializer,
# )

# from users.models import CustomUser
# from company.models import (
#     Agent,
#     Agent_type,
# )
# from transactions.models import (
#     Transaction,
#     Product_family,
# )
# from money.models import (
#     Currency,
#     Exchange_rate,
# )


# class SchBergListView(ListCreateAPIView):

#     ''' Correctly sets the "by" Custom user field. '''

#     def pre_save(self, obj):
#         obj.by = self.request.user


# class UserCreateReadView(ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser, )


# class UserReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser, )


# class AgentTypeCreateReadView(SchBergListView):
#     queryset = Agent_type.objects.all()
#     serializer_class = AgentTypeSerializer
#     permission_classes = (IsAdminUser, )


# class AgentTypeReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Agent_type.objects.all()
#     serializer_class = AgentTypeSerializer
#     permission_classes = (IsAdminUser, )


# class AgentCreateReadView(SchBergListView):
# # TODO: You should check that agents are not children of one anothers.
# # Otherwise you'll have infinte recurision.
#     queryset = Agent.objects.all()
#     serializer_class = AgentSerializer
#     permission_classes = (IsAuthenticated, )


# class AgentsForUserCreateReadView(ListAPIView):
#     serializer_class = AgentSerializer
#     permission_classes = (IsAuthenticated, )

#     def get_queryset(self):
#         user = self.request.user.id
#         return Agent.objects.filter(user=user)


# class AgentReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Agent.objects.all()
#     serializer_class = AgentSerializer
#     permission_classes = (IsAdminUser, )


# class TransactionCreateReadView(SchBergListView):
#     # Ensure when creating a transaction, that agent_from.user is the posting
#     # user.
#     serializer_class = TransactionSerializer
#     permission_classes = (IsAuthenticated, )

#     def get_queryset(self):
#         if self.request.GET.get('agentId'):
#             agentId = int(self.request.GET.get('agentId'))
#             return Transaction.objects.filter(from_agent=agentId)
#         return Transaction.objects.all()


# class TransactionReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#     permission_classes = (IsAuthenticated, )

