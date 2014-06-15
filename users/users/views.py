import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from users.models import CustomUser
# your views here.


@api_view(['GET', ])
def is_admin(request):
    if hasattr(request, 'auth') and hasattr(request.user, 'is_admin'):
        res = {'is_admin': request.user.is_admin, }
        return HttpResponse(json.dumps(res))
    return HttpResponse('You must be logged in.')


@csrf_exempt
@api_view(['GET', ])
def set_password(request, pk=None):
    if hasattr(request, 'auth') and hasattr(request.user, 'is_admin'):
        user = CustomUser.objects.filter(id=pk).first()
        if request.GET['password'] and user is not None:
            password = request.GET['password']
            user.set_password(password)
            user.save()
            res = {'success': True, }
            return HttpResponse(json.dumps(res))
        res = {'success': False, }
        return HttpResponse(json.dumps(res))
    return HttpResponse('You must be logged in and admin.')
