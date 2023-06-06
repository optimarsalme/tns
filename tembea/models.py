from django.db import models

# Create your models here.
class Services(models.Model):
    serviceName     = models.CharField(max_length=20)
    description     = models.CharField(max_length=150)
    image           = models.ImageField(upload_to='Tembea/services/images')

    def __str__(self):
        return self.serviceName

class Gallery(models.Model):
    title           = models.CharField(max_length=30)
    image           = models.ImageField(upload_to='Tembea/gallery/images')

    def __str__(self):
        return self.title
        