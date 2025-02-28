from django.shortcuts import render, redirect, HttpResponse
from .models import Services

# Create your views here.
def services_view(request):

    services_all = Services.objects.all()

    return render(request, 'services.html', {'services_all' : services_all})