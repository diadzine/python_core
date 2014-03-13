#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.core.serializers import serialize

from pages.models import Pages
from users.views import isLoggedIn


def get(request):
    if request.GET.get('id'):
        pagesId = request.GET.get('id')
        pages = Pages.objects.filter(id=pagesId)

    else:
        pages = Pages.objects.all().order_by('date').reverse()

    return HttpResponse(serialize('json', pages))


def delete(request):
    pagesId = request.GET.get('id')
    if pagesId:
        if isLoggedIn(request):
            pages = Pages.objects.filter(id=pagesId)
            pages.delete()
            return HttpResponse('1')
    return HttpResponse('0')


def save(request):
    if isLoggedIn(request):
        req = request.GET
        id = req.get('id')
        title = req.get('title')
        content = req.get('content')
        mag = req.get('mag')
        if id:
            pages = Pages.objects.filter(id=id)
            pages = pages.first()
        else:
            pages = Pages()
        pages.title = title
        pages.content = content
        pages.mag = mag
        pages.save()
        return HttpResponse('1')
    return HttpResponse('0')
    