from django.shortcuts import render
from .forms import login
from django.http import HttpResponseRedirect
from .models import profile
def  user_login(request):
    if request.method == "POST":
        form=login(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']
            pa=form.cleaned_data['password']
        
            # save data in data base
            user= profile(name=nm ,email=em ,password=pa)
            user.save()

            # update data
            user=profile(id=1,name=nm,email=em,password=pa)
            # user.save()

            # delete data
            user=profile(id=1)
            # user.delete()
            return HttpResponseRedirect('/home/login/')

        
    else:
        form=login()

    return render(request,'app1/login.html',{"form":form})         