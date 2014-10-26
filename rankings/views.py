#-*- coding: utf-8 -*-
import ujson

from django.http import HttpResponse, Http404
from django.core.cache import cache
from django.db import connection

RACES_PER_VIEW = 25


def last_races(request):
    cursor = connection.cursor()
    query = "SELECT id, info, category, genre, link, location, discipline, raceId, date FROM rankings_races ORDER BY date DESC LIMIT " + \
        str(RACES_PER_VIEW) + ";"
    cursor.execute(query)
    races = dictfetchall(cursor)
    races = ujson.dumps(races, encode_html_chars=False, ensure_ascii=False)
    res = HttpResponse(
        races,
        content_type="application/json"
    )
    return res


def race(request, pk):
    pk = str(int(pk))
    cursor = connection.cursor()
    query = "SELECT id, info, category, genre, link, location, discipline, `table`, raceId, date FROM rankings_races WHERE id='" + \
        pk + "';"
    cursor.execute(query)
    races = dictfetchall(cursor)[0]
    races = ujson.dumps(races, encode_html_chars=False, ensure_ascii=False)
    res = HttpResponse(
        races,
        content_type="application/json"
    )
    return res


def race_category(request, category):
    if category not in ['WC', 'EC', 'FIS']:
        return Http404
    page = request.GET.get('page')
    page = 0 if page is None else int(page - 1)
    offset = RACES_PER_VIEW * page
    cursor = connection.cursor()
    query = "SELECT id, info, category, genre, link, location, discipline, raceId, date FROM rankings_races WHERE category='" + \
        category + "' ORDER BY date DESC LIMIT " + \
            str(offset) + ", " + str(RACES_PER_VIEW) + ";"
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
