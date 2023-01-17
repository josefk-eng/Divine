from django.db import models

# Create your models here.
class ministry(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    story = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=200, blank=True)
    number = models.CharField(max_length=200, blank=True)
    
    def __str__(self) -> str:
        return self.name
