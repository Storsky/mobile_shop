from django.contrib import admin
from .models import Brand, Product, PhoneReview

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class ReviewAdmin(admin.TabularInline):
    model = PhoneReview

class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewAdmin,]
    list_display = ['name', 'brand', 'specs', 'image', 'description']



admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PhoneReview)
