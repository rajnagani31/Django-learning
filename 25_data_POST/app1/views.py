from django.shortcuts import render
from app1.forms import login
from django.http import HttpResponseRedirect
# Create your views here.
def account_login(request):
    if request.method ==  'POST': # POST only capital
       form=login(request.POST)
       if (form.is_valid()):      # They define true and false
           print(form.cleaned_data)

           print(f"Full name:{form.cleaned_data["Full_name"]}")
           print(f"email:{form.cleaned_data["email"]}")
           print(f"password:{form.cleaned_data["password"]}")
           return HttpResponseRedirect('/home/success/')
    else:
        form=login()
    return render(request,'app1/login.html',{'form':form})


def success(req):
    return render (req,'app1/success.html')