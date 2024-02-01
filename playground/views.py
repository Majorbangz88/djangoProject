from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def welcome(requests):
    return HttpResponse("Welcome to django")


def hello_user(request, name):
    return render(request, 'hello.html', {"name": name})


def one(request, number):
    return HttpResponse(number)
