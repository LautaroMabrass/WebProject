from django.shortcuts import render,redirect
from .forms import newForm
from django.core.mail import EmailMessage

# Create your views here.

def contact_view(request):
    if request.method == 'GET':
        return render(request, 'contact.html', {'new_form': newForm()})
    else:
        form_ = newForm(data=request.POST)
        if form_.is_valid():
            name = request.POST['name']
            client_email = request.POST['email']
            content = request.POST['content']

            email = EmailMessage(
                f'Message from Client {name}',
                f'A client with the email address {client_email} sent the following message: \n {content}',
                'Contacto Web <appwebmail2025@gmail.com>',
                ['appwebmail2025@gmail.com'],
                reply_to=[client_email],
            )

            try:
                email.send()
                return redirect('/contact/?valid')
            except:
                return redirect('/contact/?notvalid')
