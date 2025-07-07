from django.shortcuts import render
from .forms import ckform

# Create your views here.

def home(request):
    fm=ckform()
    return render(request,'CK/home.html',{'form':fm})
