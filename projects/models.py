from unicodedata import name
from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    resource_url = models.URLField()
    description = models.CharField(max_length=300)
