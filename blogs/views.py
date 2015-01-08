#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.contrib.syndication.views import Feed
from django.utils import timezone

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
    if request.GET.get('id'):
        postId = request.GET.get('id')
        post = BlogPosts.objects.filter(id=postId)

    else:
        post = BlogPosts.objects.all().order_by('date').reverse()

    return HttpResponse(serialize('json', post))


def blogId(request):
    blogId = request.GET.get('blogId')
    post = BlogPosts.objects.filter(blogId=blogId).order_by('date').reverse()

    return HttpResponse(serialize('json', post))


@csrf_exempt
def saveBlogger(request):
    if isLoggedIn(request):
        req = request.POST
        id = req.get('id')
        name = req.get('name')
        biography = req.get('biography')
        linkResults = req.get('linkResults')
        profilePic = req.get('profilePic')
        sponsors = req.get('sponsors')
        ad = req.get('ad')
        if not int(id) == 0:
            blogger = Bloggers.objects.filter(id=id).first()
        else:
            blogger = Bloggers()
        if name:
            blogger.name = name
            blogger.biography = biography
            blogger.linkResults = linkResults
            blogger.profilePic = profilePic
            blogger.sponsors = sponsors
            blogger.ad = ad
            blogger.save()
            id = blogger.id
            blogger = Bloggers.objects.filter(id=id)
            return HttpResponse(serialize('json', blogger))
    return HttpResponse('0')


@csrf_exempt
def savePost(request):
    if isLoggedIn(request):
        req = request.POST
        id = req.get('id')
        title = req.get('title')
        content = req.get('content')
        blogId = req.get('blogId')
        if not int(id) == 0:
            post = BlogPosts.objects.filter(id=id).first()
        else:
            post = BlogPosts()
        if title and content and blogId:
            post.title = title
            post.content = content
            post.blogId = blogId
            post.save()
            id = post.id
            post = BlogPosts.objects.filter(id=id)
            return HttpResponse(serialize('json', post))
    return HttpResponse('0')


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


class BlogsRSS(Feed):
    title = "Tooski Bloggers"
    link = "http://tooski.ch/"
    description = "Les blogs de Tooski"
    author_name = 'Tooski'
    now = timezone.now()

    def items(self):
        return BlogPosts.objects.filter(date__lte=self.now).order_by('date').reverse()[:25]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return 'http://tooski.ch/#!/Blog?id=%s' % item.blogId

    def feed_copyright(self):
        return 'Copyright 2009-2015 © seba-1511. Tous droits réservés.'
