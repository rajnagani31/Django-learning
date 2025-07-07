from django.shortcuts import render
from .forms import user_login
from django.http import HttpResponseRedirect
# Create your views here.

def login(request):
    if request.method == 'POST':
        form=user_login(request.POST)
        if form.is_valid():
            form.cleaned_data['name']
            form.cleaned_data['password']
            return HttpResponseRedirect('/home/login/')
        



    else:
        form=user_login()

    return render(request,'app1/login.html',{'form':form})        