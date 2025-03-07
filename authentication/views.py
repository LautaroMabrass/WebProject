from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

class Vregister(View):

    def get(self,request):
        form = UserCreationForm()
        return render(request, 'auth.html', {'form': form})
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = form.save() # alamcena automaticamente en auth usuario y pass encriptada

            login(request, user) # log automatico

            return redirect('home')
        else:
            return render(request, 'auth.html', {'form': form})

def close_sesion(request):
    logout(request)
    return redirect('home')

def view_close(request):
    return render(request, 'closeSesion.html')

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password_name = form.cleaned_data.get('password')
            user_pass = authenticate(username=user_name,password = password_name)
            if user_pass is not None:
                login(request, user_pass)
                return redirect('home')
            else:
                messages.error(request, 'User invalid')
        else:
            messages.error(request, 'Something goes wrong')
            
    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})