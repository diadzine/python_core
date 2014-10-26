#-*- coding: utf-8 -*-
import ujson
import time

from django.http import HttpResponse
from django.core.serializers import serialize
from django.db import connection

from rankings.models import Races

RACES_PER_VIEW = 15


def get(request):
    if request.GET.get('id'):
        racesId = request.GET.get('id')
        races = Races.objects.filter(id=racesId)

    else:
        races = Races.objects.all().order_by('date').reverse()[:25]

    return HttpResponse(serialize('json', races))


def last_races(request):
    races = Races.objects.all().order_by('date').reverse()[:RACES_PER_VIEW]
    return HttpResponse(
        serialize('json', races),
        content_type="application/json"
    )


def race(request, pk):
    race = Races.objects.filter(pk=pk).first()
    race = serialize('json', [race], ensure_ascii=False)
    race = race[1:-1]
    return HttpResponse(race, content_type="application/json")


def race_category(request, category):
    cursor = connection.cursor()
    query = "SELECT id, info, category, genre, link, location, discipline,`table`, raceId, date FROM rankings_races WHERE category='WC' ORDER BY date DESC LIMIT 10;"
    cursor.execute(query)
    races = dictfetchall(cursor)
    races = ujson.dumps(races, encode_html_chars=False, ensure_ascii=False)
    res = HttpResponse(
        races,
        content_type="application/json"
    )
    return res


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
