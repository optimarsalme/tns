from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['owner', 'category', 'subcategory', 'variation', 'product_name', 'description', 'price', 'stock', 'date_added',]

admin.site.register(Product, ProductAdmin)
