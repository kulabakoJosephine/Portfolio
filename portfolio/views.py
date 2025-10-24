from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from .models import Project

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def skills(request):
    return render(request, 'skills.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            full_message = f"From: {cd['name']} <{cd['email']}>\n\n{cd['message']}"
            
            send_mail(
                cd['subject'],                  # subject
                full_message,                   # message body
                settings.DEFAULT_FROM_EMAIL,    # sender
                [settings.CONTACT_RECEIVER_EMAIL], # recipient
            )
            return redirect('contact_success')  # redirect after sending

    return render(request, 'contact.html', {'form': form})


