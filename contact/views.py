from django.shortcuts import render,redirect
from .forms import newForm

# Create your views here.
def contact_view(request):
    if request.method == 'GET':
        return render(request, 'contact.html', {'new_form' : newForm()})
    else:
        form_ = newForm(data=request.POST)
        if form_.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            content = request.POST['content']

        print(f"{name},{email},{content}")
        return redirect('/contact/?valid')