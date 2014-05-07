#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.core.serializers import serialize

from rankings.models import Races

# Create your views here.


def get(request):
    if request.GET.get('id'):
        racesId = request.GET.get('id')
        races = Races.objects.filter(id=racesId)

    else:
        races = Races.objects.all().order_by('date').reverse()[:25]

    return HttpResponse(serialize('json', races))
