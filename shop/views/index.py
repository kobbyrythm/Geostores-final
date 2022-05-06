from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from shop.forms import BasketAddProductForm, ProductForm
from shop.models import Product
from django.core.paginator import Paginator
from django.shortcuts import render
from shop.models import Product

def index(request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 25) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/index.html', {'page_obj': page_obj})


def categories(request):
    return{'categories':Product.objects.all()}


# def index (request):
#     products = Product.objects.all()
#     return render(request,'shop/index.html', {'products': products})


    
