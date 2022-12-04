from django.shortcuts import render, redirect
from .models import Product
from django.core.paginator import Paginator

def index(request):
    return redirect('catalog')

# Create your views here.
def show_products(request):
    template = 'phones.html'
    sort = request.GET.get("sort")
    if sort=='brand':
        phones = Product.objects.order_by('brand')
    elif sort=='alphabet':
        phones = Product.objects.order_by('name')
    else:
        phones = Product.objects.all()
    
    paginator = Paginator(phones, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    context = {'phones': page_obj}

    return render(request, template, context)

def show_login_page(request):
    template = 'login.html'
    context = {}
    return render(request, template, context)

def show_model(request, product_pk):
    template = 'product.html'
    context = {'phone': Product.objects.filter(id=product_pk).values()[0]}
    return render(request, template, context)