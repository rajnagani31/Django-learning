from django.shortcuts import render
from .forms import form
from django.http import HttpResponseRedirect
# Create your views here.

def login(request):
    if request.method == "POST":
        fm=form(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['roll'])
            print(fm.cleaned_data['choice'])
            print(fm.cleaned_data['name'])
            return HttpResponseRedirect('/home/login/')
        
    else:
        fm=form()

    return render(request,'app1/login.html',{"form":fm})        
def success(req):
    return render (req,'app1/success.html')