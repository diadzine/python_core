from django.db import models

# Create your models here.

class Covers(models.Model):
    url = models.TextField(null=False)
