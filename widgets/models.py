from django.db import models

# Create your models here.


class Widgets(models.Model):
    name = models.CharField(max_length=128, null=True)
    content = models.TextField(null=True)

    def __unicode__(self):
        return u'%s' % self.name
