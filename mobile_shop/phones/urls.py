from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('catalog', show_products, name = 'catalog')
]
