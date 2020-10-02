from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'email_verify/index.html')


def verify(request):
    return render(request, 'email_verify/verify.html')


def send(request):
    return render(request, 'email_verify/send.html')
