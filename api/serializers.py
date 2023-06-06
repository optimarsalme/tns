from rest_framework import serializers
from .models import Product
from tembea.models import Services, Gallery


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Product
        fields  = [
            'pk', 'product_name', 'description', 'price', 'stock', 'date_added', 'is_available', 'image'
        ]    
        
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Services 
        fields  = ['serviceName', 'description', 'image']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model   = Gallery 
        fields  = ['title', 'image']       