#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.core.serializers import serialize

from news.models import News


def home(request):
		if request.GET.get('id'):
			newsId = request.GET.get('id')
			news = News.objects.filter(id=newsId)
		else:
	        news = News.objects.all().order_by('date').reverse()[:20]
        return HttpResponse(serialize('json', news))


def latest_entries(request):
        posts = Post.objects.all().order_by('date').reverse()[:20]
        return HttpResponse(serialize('json', posts))
