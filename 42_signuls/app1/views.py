from django.shortcuts import render,HttpResponse
from app1 import custom_signals
# Create your views here.

def  home(request):
    custom_signals.notification.send(sender='raj' ,request=request ,user=['nero','Technology'])
    return HttpResponse("Hello Home page")