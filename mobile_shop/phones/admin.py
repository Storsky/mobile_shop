from django.contrib import admin
from .models import Brand, Product

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class ProductAdmin(admin.ModelAdmin):
   
    list_display = ['name', 'brand', 'specs', 'image', 'description']



admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
