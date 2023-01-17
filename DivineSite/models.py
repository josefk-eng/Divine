from distutils.command.upload import upload
from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'img/custom')
    
    def __str__(self):
        return self.title
    