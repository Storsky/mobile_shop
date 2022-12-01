from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('catalog', show_products, name = 'catalog'),
    path('login', show_login_page, name='login_page'),
    path('catalog/model/<int:model_id>', show_model, name='model')
]
