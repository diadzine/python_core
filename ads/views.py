import HttpResponse
import serialize
import cloudinary

from django.views.decorators.csrf import csrf_exempt
from cloudinary import (
    uploader,
    api,
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
    if request.FILES and request.FILES['file']:
        image = request.FILES['file']
        uploaded = uploader.upload(image,
                                   eager=[
                                       # Each eager will be automatically created when the
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
        ad.secureUrl = uploaded['securle_url']
        ad.horizontal = 0
        ad.vertical = 0
        ad.square = 1
        ad.save()
        return HttpResponse(serialize('json', ad))
