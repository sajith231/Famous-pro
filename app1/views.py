from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .utils import send_contact_email

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form
            contact = form.save()
            
            # Send email
            email_sent = send_contact_email(form.cleaned_data)
            
            if email_sent:
                messages.success(request, 'Your message has been sent successfully!')
            else:
                messages.warning(request, 'Your message was saved but there was an error sending the email notification.')
                   
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'app1/index.html', {'form': form})
    

# product page is the main div of  the whole sector

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form
            contact = form.save()
            
            # Send email
            email_sent = send_contact_email(form.cleaned_data)
            
            if email_sent:
                messages.success(request, 'Your message has been sent successfully!')
            else:
                messages.warning(request, 'Your message was saved but there was an error sending the email notification.')
            
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'app1/contact.html', {'form': form})


    




def product(request):
    return render(request,'app1/product.html') 
















