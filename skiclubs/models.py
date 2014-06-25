from django.db import models

# Create your models here.


class Skiclubs(models.Model):
    title = models.CharField(max_length=510)
    latitude = models.TextField(null=True)
    longitude = models.TextField(null=True)
    contact = models.TextField(null=True)
    description = models.TextField(null=True)

    def __unicode__(self):
        return u'%s' % self.name
