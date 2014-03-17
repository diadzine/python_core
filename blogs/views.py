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
        blogs = Bloggers.objects.all().order_by('date').reverse()

    return HttpResponse(serialize('json', blogs))


def posts(request):
	# Handle blogId and postId case.
    if request.GET.get('id'):
        postId = request.GET.get('id')
        post = BlogPosts.objects.filter(id=postId)

    else:
        post = BlogPosts.objects.all().order_by('date').reverse()[:20]

    return HttpResponse(serialize('json', post))


def saveBlogger(request):
    return True

def savePost(request):
    return True

def deleteBlogger(request):
    bloggerId = int(request.GET.get('id'))
    if bloggerId:
        if isLoggedIn(request):
            blogger = Bloggers.objects.filter(id=bloggerId)
            blogger.delete()
            return HttpResponse('1')
    return HttpResponse('0')

def deletePost(request):
    postId = int(request.GET.get('id'))
    if postId:
        if isLoggedIn(request):
            post = BlogPosts.objects.filter(id=postId)
            post.delete()
            return HttpResponse('1')
    return HttpResponse('0')