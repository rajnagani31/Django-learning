from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfunc(request):
    return HttpResponse("<h1>Nero technology</h1>")

def home(request):
    return HttpResponse("HOME ")

def my_math(request):
    a=30*30
    return HttpResponse(a)

def learn_lengchian(request):
    learn='<h1> <i>learn leng chain </h1></i>'
    return HttpResponse(learn)