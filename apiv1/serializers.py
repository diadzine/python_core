from rest_framework import serializers
from news.models import News
from ads.models import Ads
from skiclubs.models import Skiclubs
from pages.models import Pages
from rankings.models import Races
from widgets.models import Widgets
from angulation.models import Covers
from blogs.models import (
    Bloggers,
    BlogPosts,
)


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'author', 'content', 'mag', 'date', )


class AdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ads
        fields = ('id', 'name', 'url', 'secureUrl',
                  'horizontal', 'vertical', 'square', 'date', )


class BloggersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bloggers
        fields = ('id', 'name', 'biography', 'linkResults',
                  'profilePic', 'sponsors', 'ad', 'date', )


class BlogPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPosts
        fields = ('id', 'title', 'content', 'blogId', 'date', )


class SkiclubsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skiclubs
        fields = (
            'id', 'title', 'latitude', 'longitude', 'contact', 'description', )


class PagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pages
        fields = ('id', 'name', 'content', 'date', )


class RacesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Races
        fields = ('id', 'info', 'category', 'genre', 'link',
                  'location', 'discipline', 'raceId', 'table', 'date', )


class WidgetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Widgets
        fields = ('id', 'name', 'content', )


class CoversSerializer(serializers.ModelSerializer):

    class Meta:
        model = Covers
        fields = ('id', 'url', )
