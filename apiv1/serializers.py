from rest_framework import serializers
from news.models import News
from ads.models import Ads


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'author', 'content', 'mag', 'date', )


class AdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ads
        fields = ('id', 'name', 'url', 'secureUrl',
                  'horizontal', 'vertical', 'square', 'date', )
