from django.db import models

# Create your models here.


class Ads(models.Model):
    name = models.CharField(max_length=510)
    url = models.TextField(null=True)
    secureUrl = models.TextField(null=True)
    horizontal = models.PositiveSmallIntegerField(null=True)
    vertical = models.PositiveSmallIntegerField(null=True)
    square = models.PositiveSmallIntegerField(null=True)
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __unicode__(self):
        return u'%s' % self.name
