from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("this is home")


def problem(request):
    return HttpResponse("this is problem's page")


def submission(request):
    return HttpResponse("this is submission page")

# Create your views here.
