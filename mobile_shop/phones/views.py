from django.shortcuts import render, redirect
from .models import Product, ProfileProduct
from django.core.paginator import Paginator
from users.models import Profile
from django.contrib import messages as messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm as rf
from users.models import Profile


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

def show_product(request, product_pk):
    template = 'product.html'
    phone = Product.objects.filter(id=product_pk)[0]
    reviews = phone.reviews.all()
    new_review = None
    if request.method == 'POST':
        review_form = rf(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.phone = phone
            new_review.user = request.user.profile
            new_review.save()
    else:
        review_form = rf()       
    context = {'phone': phone, 'reviews': reviews, 'new_review': new_review, 'review_form': rf} 
    return render(request, template, context)


@login_required
def buy_product(request, product_pk, action):
    if action == 'buy':
        current_user = request.user.id
        new_order = ProfileProduct(profile = Profile.objects.get(pk=current_user), product = Product.objects.get(pk=product_pk))
        new_order.save()
        messages.success(request, f'Вы купили {Product.objects.get(pk=product_pk)}')
    return redirect ('catalog')