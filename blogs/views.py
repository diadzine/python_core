#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.core.serializers import serialize

from blogs.models import Bloggers, BlogPosts
from users.views import isLoggedIn


def bloggers(request):
    if request.GET.get('id'):
        blogsId = request.GET.get('id')
        blogs = Bloggers.objects.filter(id=blogsId)

    else:
        blogs = Bloggers.objects.all().order_by('date').reverse()[:20]

    return HttpResponse(serialize('json', blogs))


def posts(request):
	# Handle blogId and postId case.
    if request.GET.get('id'):
        postId = request.GET.get('id')
        post = BlogPosts.objects.filter(id=postId)

    else:
        post = BlogPosts.objects.all().order_by('date').reverse()[:20]

    return HttpResponse(serialize('json', post))