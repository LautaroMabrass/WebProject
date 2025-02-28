from django.shortcuts import render, redirect, HttpResponse
from services.models import Services

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def store_view(request):
    return render(request, 'store.html')

def blog_view(request):
    return render(request, 'blog.html')

def contact_view(request):
    return render(request, 'contact.html')