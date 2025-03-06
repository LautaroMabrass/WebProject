from django.shortcuts import render,redirect
from .shopingcart import ShoppingCart
from store.models import products

# Create your views here.

def add_product(request, product_id):
    shopping = ShoppingCart(request)

    product = products.objects.get(id=product_id)

    shopping.add(product)
    
    return redirect('store')

def delete_product(request, product_id):
    shopping = ShoppingCart(request)

    product = products.objects.get(id=product_id)

    shopping.delete(product)

    return redirect('store')

def less_product(request, product_id):
    shopping = ShoppingCart(request)

    product = products.objects.get(id=product_id)

    shopping.less_amount(product)

    return redirect('store')

def clean_product(request):
    shopping = ShoppingCart(request)

    shopping.clean()

    return redirect('store')


