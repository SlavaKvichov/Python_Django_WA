from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'users/login.html', {
        'page': 'login'
    })

def register(request):
    return render(request, 'users/register.html', {
        'page': 'register'
    })