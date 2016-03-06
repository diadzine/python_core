from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField


class Ads(models.Model):
    name = models.CharField(max_length=510)
    url = models.TextField(null=True)
    secureUrl = models.TextField(null=True)
    link = models.TextField(null=True, default='')
    placeholders = MultiSelectField(choices=settings.ADS_PLACEHOLDERS)
    horizontal = models.PositiveSmallIntegerField(null=True)
    vertical = models.PositiveSmallIntegerField(null=True)
    square = models.PositiveSmallIntegerField(null=True)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.name
