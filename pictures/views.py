import cloudinary

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from cloudinary import (
    uploader,
)


def connect():
    cloudinary.config(
        cloud_name='tooski',
        api_key='664376587529146',
        api_secret='YHcBvOXBRmOroGCAxnpx_e5jFp0',
    )


@api_view(['GET', 'POST', 'PUT', 'DELETE', ])
@csrf_exempt
def upload(request):
    if hasattr(request, 'auth') and hasattr(request.user, 'is_admin'):
        connect()
        if request.FILES.get('file'):
            image = request.FILES.get('file')
            uploaded = uploader.upload(image,
                                       eager=[
                                           # Each eager will be automatically
                                           #  created when the
                                           # file is uploaded. Could be usefull
                                           # for
                                           {
                                               'width': 650,
                                               'height': 280,
                                               'crop': 'thumb',
                                               'gravity': 'face',
                                           },
                                           {
                                               'width': 700,
                                               'height': 280,
                                               'crop': 'thumb',
                                               'gravity': 'face',
                                           },
                                           {
                                               'width': 1800,
                                               'height': 280,
                                               'crop': 'thumb',
                                               'gravity': 'face',
                                           },
                                           {
                                               'width': 500,
                                               'height': 280,
                                               'crop': 'thumb',
                                               'gravity': 'face',
                                           }
                                       ])
            return HttpResponse(uploaded['url'])
        return HttpResponse('No image received...')
    return HttpResponse('Not connected')
