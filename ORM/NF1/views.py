from django.shortcuts import render
from .forms import corseform
# Create your views here.

def form(request):
    form=corseform()
    return render(request,'NF1/nf1.html',{'form':form})