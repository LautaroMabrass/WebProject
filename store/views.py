from django.shortcuts import render
from .models import products
from django.core.mail import EmailMessage
# Create your views here.

def store_view(request):
    products_all = products.objects.all()
    
    return render(request, 'store.html', {'products_all' : products_all})

def buy_everything(request):
    pass