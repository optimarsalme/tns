from django.db import models
from django.db import models
from django.utils import timezone
from accounts.models import Account

class Product(models.Model):
    owner               = models.ForeignKey(Account, on_delete=models.CASCADE) 
    category            = models.CharField(max_length=15)
    subcategory         = models.CharField(max_length=15)
    variation           = models.CharField(max_length=15)
    
    product_name        = models.CharField(max_length=50)
    description         = models.TextField(max_length=250)
    price               = models.IntegerField()
    stock               = models.IntegerField()
    date_added          = models.DateTimeField(default=timezone.now)
    is_available        = models.BooleanField(default=True)
    image               = models.ImageField(upload_to='images/products')

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.product_name



