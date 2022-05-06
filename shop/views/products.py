from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from shop.forms import BasketAddProductForm, ProductForm
from shop.models import Product

def product_list(request):
    products = Product.objects.all()    
    return render(request, 'shop/product_list.html', {'products' : products })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket_product_form = BasketAddProductForm()
    return render(request, 'shop/product_detail.html', {'product' : product,'basket_product_form': basket_product_form})
