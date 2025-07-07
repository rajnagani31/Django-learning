from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("HOME PAGE")

def app1(request):
    return HttpResponse("app1 page")


