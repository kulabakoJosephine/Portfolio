from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from .models import Project


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def skills(request):
    return render(request, 'skills.html')


def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            full_message = (
                f"From: {cd['name']} <{cd['email']}>\n\n"
                f"{cd['message']}"
            )

            send_mail(
                subject=cd['subject'],
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
            )

            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm()  # reset form

    return render(request, 'contact.html', {'form': form})
