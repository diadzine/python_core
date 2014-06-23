from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cloudinary import (
    uploader,
)

from ads.models import Ads
from pictures.views import connect


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
        ad.horizontal = 1 if request.POST.get('horizontal') == 'true' else 0
        ad.vertical = 1 if request.POST.get('vertical') == 'true' else 0
        ad.square = 1 if request.POST.get('square') == 'true' else 0
        ad.save()
        return HttpResponse(ad.url)
    return HttpResponse('No image received...')


def get():
    pass


def delete():
    pass
