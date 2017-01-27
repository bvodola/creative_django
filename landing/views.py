from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'landing/home.html', {})

def services(request):
    return render(request, 'landing/services.html', {})

def portfolio(request):
    return render(request, 'landing/portfolio.html', {})

def contact(request):
    return render(request, 'landing/contact.html', {})
