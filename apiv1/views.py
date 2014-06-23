from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from apiv1.serializers import (
    NewsSerializer,
)

from news.models import News


class SchBergListView(ListCreateAPIView):

    ''' Correctly sets the "by" Custom user field. '''

    def pre_save(self, obj):
        obj.by = self.request.user


class NewsCreateReadView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class NewsReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


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

