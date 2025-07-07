from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2(request,**kwargs):
    status=kwargs.get('status')

    return HttpResponse(f'hello home {status}')