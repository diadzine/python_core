#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.contrib.syndication.views import Feed
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from news.models import News
from users.views import isLoggedIn


def home(request):
    if request.GET.get('id'):
        newsId = request.GET.get('id')
        news = News.objects.filter(id=newsId)

    else:
        news = News.objects.all().order_by('date').reverse()[:50]

    return HttpResponse(serialize('json', news))


def delete(request):
    newsId = int(request.GET.get('id'))
    if newsId:
        if isLoggedIn(request):
            news = News.objects.filter(id=newsId)
            news.delete()
            return HttpResponse('1')
    return HttpResponse('0')


@csrf_exempt
def save(request):
    if isLoggedIn(request):
        req = request.POST
        id = req.get('id')
        title = req.get('title')
        content = req.get('content')
        mag = req.get('mag')
        signature = request.COOKIES.get('signature')
        if not int(id) == 0:
            news = News.objects.filter(id=id).first()
        else:
            news = News()
        if title and content and mag:
            news.title = title
            news.content = content
            news.mag = mag
            news.author = signature
            news.save()
            id = news.id
            news = News.objects.filter(id=id)
            return HttpResponse(serialize('json', news))
    return HttpResponse('0')


class RSSFeed(Feed):
    title = "Tooski.ch"
    link = "http://www.tooski.ch/"
    description = "Actualité sur la coupe du monde FIS de ski alpin."
    author_name = 'Tooski'
    now = timezone.now()

    def items(self):
        return News.objects.filter(date__lte=self.now).order_by('date').reverse()[:25]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return 'http://www.tooski.ch/#!/News?n=%s' % item.id

    def feed_copyright(self):
        return 'Copyright 2009-2014 © seba-1511. Tous droits réservés.'
