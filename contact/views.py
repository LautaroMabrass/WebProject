from django.shortcuts import render,redirect
from .forms import newForm

# Create your views here.
def contact_view(request):
    return render(request, 'contact.html', {'new_form' : newForm()})