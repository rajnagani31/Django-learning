from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2(request):
    return HttpResponse("app2 page")

def app2_new(request):
    return HttpResponse("app2 new page")

