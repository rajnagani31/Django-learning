from django.shortcuts import render
from datetime import datetime,timedelta,timezone
# Create your views here.


def set_cooki(request):

    response= render(request,'app1/01_set_cookies.html')
    
    # response.set_cookie("Token",'value ok',max_age=3600) # max age the refur validate cooki time in secoun 3600 mean 1 hour valdate cookie
    response.set_cookie("Token","value ok",expires=datetime.now(timezone.utc) + timedelta(days=2))
    return response

def get_cooki(request):
    id=request.COOKIES.get('Token',"defulat_value_return")  # set cooki not set after get cooik return defualt value and defulat value are not set get method return None
    return render(request,'app1/02_get_cookies.html',{'id':id})


def delete_cooki(request):
    response=render(request,'app1/03_delete_cookies.html')    
    response.delete_cookie('Token')
    return response

def set_signed(request):
    response=render(request,'app1/04_set_signed_cookies.html')
    response.set_signed_cookie('admin','ok cooki',salt='ad')
    return response

def get_signed(request):
    token=request.get_signed_cookie('admin',default="it's ok default",salt='ad')#defult set using defailt key
    return render(request,'app1/05_get_signed_cookies.html',{'id':token})
