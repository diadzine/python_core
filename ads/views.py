import cloudinary

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cloudinary import (
    uploader,
)

from ads.models import Ads


def connect():
    cloudinary.config(
        cloud_name='tooski',
        api_key='664376587529146',
        api_secret='YHcBvOXBRmOroGCAxnpx_e5jFp0',
    )


@csrf_exempt
def save(request):
    # Check if user is connected.
    connect()
    if request.FILES.get('file'):
        image = request.FILES.get('file')
        uploaded = uploader.upload(image,
                                   eager=[
                                       # Each eager will be automatically
                                       #  created when the
                                       # file is uploaded. Could be usefull for
                                       # {
                                       #     'width': 200,
                                       #     'height': 200,
                                       #     'crop': 'thumb',
                                       #     'gravity': 'face',
                                       # },
                                   ])
        ad = Ads()
        ad.name = uploaded['public_id']
        ad.url = uploaded['url']
        ad.secureUrl = uploaded['secure_url']
        ad.horizontal = request.POST.get('horizontal')
        ad.vertical = request.POST.get('vertical')
        ad.square = request.POST.get('square')
        ad.save()
        return HttpResponse(ad.url)
    return HttpResponse('No image received...')


def get():
    pass


def delete():
    pass
