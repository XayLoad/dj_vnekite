from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegForm, AuthForm


def index(request):
    return render(request, 'auth/login.html', {
        "RegForm": RegForm,
        "AuthForm": AuthForm
    })
