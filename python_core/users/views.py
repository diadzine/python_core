#-*- coding: utf-8 -*-

from time import strftime

from django.http import HttpResponse, Http404
from django.core.serializers import serialize

from users.models import Users


def login(request):
	req = request.GET
	email = req.get('email')
	password = req.get('password')
	user = Users.objects.filter(email=email).first()
	if user and user.password == str(hash(password)):
		token = user.token = hash(strftime("%H:%M:%S"))
		return HttpResponse('{email: ' + email + ', token: \'' + str(token) + '\', success: 1}')
	else:
		return HttpResponse('{success: 0}');


def delete(request):
    usersId = request.GET.get('id')
    if usersId:
        # Check if logged in !
        users = Users.objects.filter(id=usersId)
        users.delete()
        return HttpResponse('1')
    else:
        return HttpResponse('0')


def save(request):
    # Check if logged in !
    req = request.GET
    id = req.get('id')
    title = req.get('title')
    content = req.get('content')
    mag = req.get('mag')
    if id:
        users = Users.objects.filter(id=id)
        users = users.first()
    else:
        users = Users()
    users.title = title
    users.content = content
    users.mag = mag
    users.save()
    return HttpResponse('1')
