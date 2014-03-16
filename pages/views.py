#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def save(request):
    if isLoggedIn(request):
        req = request.POST
        id = req.get('id')
        name = req.get('name')
        content = req.get('content')
        if not int(id) == 0:
            page = Pages.objects.filter(id=id).first()
        else:
            page = Pages()
        if name and content:
            page.name = name
            page.content = content
            page.save()
            id = page.id
            page = Pages.objects.filter(id=id)
            return HttpResponse(serialize('json', page))
    return HttpResponse('0')