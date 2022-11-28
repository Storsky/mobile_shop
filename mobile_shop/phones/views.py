from django.shortcuts import render, redirect
from .models import Model_id
def index(request):
    return redirect('catalog')

# Create your views here.
def show_products(request):
    template = 'phones.html'
    context = {'phones': Model_id.objects.all()}
    return render(request, template, context)