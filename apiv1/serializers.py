# from rest_framework import serializers
# from users.models import CustomUser
# from company.models import (
#     Agent,
#     Agent_type,
# )
# from transactions.models import (
#     Transaction,
#     Transaction_type,
#     Product_family,
# )
# from money.models import (
#     Currency,
#     Exchange_rate,
# )


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CustomUser
#         fields = ('id', 'is_admin', 'email', 'name')


# class AgentTypeSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Agent_type
#         fields = ('id', 'name',)


# class AgentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Agent
#         fields = ('id', 'name', 'parent', 'type', 'user', )
