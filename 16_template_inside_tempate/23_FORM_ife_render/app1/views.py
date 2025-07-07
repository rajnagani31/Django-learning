from django.shortcuts import render
from app1.forms import registration,address,Login
# Create your views here.

def register(request):
    fm=registration(auto_id=True,initial={"Email":"123abc@gmail.com"})
    return render(request,'app1/form.html',{'form':fm})

def add(request):
    fm=address()
    return render(request,'app1/address.html',{'form':fm})


def login(request):
    fm=Login()
    return render(request,"app1/login.html",{"form":fm})    