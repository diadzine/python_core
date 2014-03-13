#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.core.serializers import serialize

from blogs.models import Bloggers, BlogPosts
from users.views import isLoggedIn


def bloggers(request):
    if request.GET.get('id'):
        blogsId = request.GET.get('id')
        blogs = News.objects.filter(id=blogsId)

    else:
        blogs = News.objects.all().order_by('date').reverse()[:20]

    return HttpResponse(serialize('json', blogs))


def posts(request):
	# Handle blogId and postId case.
    if request.GET.get('id'):
        postId = request.GET.get('id')
        post = News.objects.filter(id=postId)

    else:
        post = News.objects.all().order_by('date').reverse()[:20]

    return HttpResponse(serialize('json', post))