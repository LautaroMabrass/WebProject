from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def store_view(request):
    return render(request, 'store.html')
