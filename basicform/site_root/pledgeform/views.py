from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PledgeForm
from django.contrib import messages

def homepage(request):
    return render(request, 'pledgeform/index.html')

def pledge_create_view(request):
    form = PledgeForm(request.POST or None)
    if form.is_valid():
        form.save()
        first_name = form.cleaned_data.get('first_name')
        amount = form.cleaned_data.get('amount')
        email = form.cleaned_data.get('email')
        subject = 'Your Pledge with Us'
        message = f'{first_name}, we have received your ${amount} pledge. /n Thank you for your support!'
        from_email = settings.EMAIL_HOST_USER
        to_list = [{email}]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        messages.success(request, f"{first_name}, thank you for your ${amount} pledge!")
        form = PledgeForm()
    context = {
        'form': form
    }
    return render(request, 'pledgeform/pledge_create.html', context)
