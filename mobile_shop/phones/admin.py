from django.contrib import admin
from .models import Brand, Model_id, Phone

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class Model_idAdmin(admin.ModelAdmin):
   
    list_display = ['name', 'brand', 'specs', 'image', 'description']

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['title', 'model_id', 'quantity', 'color', 'price']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Model_id, Model_idAdmin)
admin.site.register(Phone, PhoneAdmin)