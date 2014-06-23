from rest_framework import serializers
from news.models import (
    News,
)


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'author', 'content', 'mag', 'date', )


# class AgentTypeSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Agent_type
#         fields = ('id', 'name',)


# class AgentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Agent
#         fields = ('id', 'name', 'parent', 'type', 'user', )
