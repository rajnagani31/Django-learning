from django.shortcuts import render
from .forms import login
from django.http import HttpResponseRedirect

def user_login(request):
    if request.method== 'POST':
        form=login(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['city'])
            return HttpResponseRedirect('/home/login/')
    else:
        form=login()    
    return render(request,'app1/login.html',{'form':form})

def success_submit(req):
    return render(req,'app1/success.html')