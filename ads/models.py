from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField


class AdsManager(models.Manager):
    def get_queryset(self):
        return super(AdsManager, self).get_queryset()

    def by_placeholder(self, placeholder):
        return super(AdsManager, self).get_queryset().filter(
            placeholders__contains=placeholder
        )

    def by_category(self, category):

        if category == 'square':
            qs = super(AdsManager, self).get_queryset().filter(square=1)
        elif category == 'horizontal':
            qs = super(AdsManager, self).get_queryset().filter(horizontal=1)
        elif category == 'vertical':
            qs = super(AdsManager, self).get_queryset().filter(vertical=1)
        else:
            qs = super(AdsManager, self).get_queryset()

        return qs

    def by_placeholder_and_category(self, placeholder, category):
        criteria = {
            'placeholders__contains': placeholder,
            category: 1,
        }
        qs = super(AdsManager, self).get_queryset().filter(**criteria)

        return qs


class Ads(models.Model):
    name = models.CharField(max_length=510)
    url = models.TextField(null=True)
    secureUrl = models.TextField(null=True)
    link = models.TextField(null=True, default='')
    placeholders = MultiSelectField(
        choices=settings.ADS_PLACEHOLDERS,
        null=True,
        blank=True,
    )
    horizontal = models.PositiveSmallIntegerField(null=True)
    vertical = models.PositiveSmallIntegerField(null=True)
    square = models.PositiveSmallIntegerField(null=True)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    objects = AdsManager()

    def __unicode__(self):
        return u'%s' % self.name


class Placeholder(object):

    def __init__(self, code, label):
        self.code = code
        self.label = label
