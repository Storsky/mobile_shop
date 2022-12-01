from django.shortcuts import render, redirect
from .models import Model_id
def index(request):
    return redirect('catalog')

# Create your views here.
def show_products(request):
    template = 'phones.html'
    sort = request.GET.get("sort")
    if sort=='brand':
        phones = Model_id.objects.order_by('brand')
    elif sort=='alphabet':
        phones = Model_id.objects.order_by('name')
    else:
        phones = Model_id.objects.all()
    context = {'phones': phones}
    return render(request, template, context)

def show_login_page(request):
    template = 'login.html'
    context = {}
    return render(request, template, context)

def show_model(request, model_id):
    template = 'product.html'
    context = {'phone': Model_id.objects.filter(id=model_id).values()[0]}
    return render(request, template, context)