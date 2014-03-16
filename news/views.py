#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

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
        print title, content, id, mag, signature
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
        else:
            return HttpResponse('0')
    return HttpResponse('0')