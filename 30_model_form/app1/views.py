from django.shortcuts import render
from .forms import login 
from django.http import HttpResponseRedirect
from .models import profile
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form=login(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']  
            pw=form.cleaned_data['password']
    # method 1
            # data save in data base
            pr=profile(name=nm,email=em,password=pw)
            pr.save()

            # data update in database
            pr=profile(id=1,name=nm,email=em,password=pw)
            pr.save()

            # delete
            pr=profile(id=2)
            pr.delete()
            return HttpResponseRedirect('/home/login/')
    # method 2
    # if request.method == 'POST':
    #     obj=profile.objects.get(pk=1)
    #     form=login(request.POST,instance=obj)
    #     if form.is_valid():
    #         form.save()
    
    #         return HttpResponseRedirect('/home/login/')        
                   



    else:

        form=login()
        # data=
    return render(request,'app1/login.html',{'form':form})

