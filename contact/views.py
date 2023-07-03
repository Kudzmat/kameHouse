from django.shortcuts import render
from .models import *


# Create your views here.

# contact page
def contact(request):

    # if a message is posted
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_form_data = ContactForm(name=name,email=email,subject=subject,message=message)  # create a new contact form object
        contact_form_data.save()

    contact_data = ContactList.objects.all()[0]  # contact info, object at index 0

    context = {
        'info': contact_data,
    }

    return render(request, 'contact.html', context)
