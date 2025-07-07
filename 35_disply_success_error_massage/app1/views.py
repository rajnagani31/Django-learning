from django.shortcuts import render
from django.contrib import messages
from .forms import login
# Create your views here.
def home(req):
    # message write one method


    # messages.add_message(req,messages.SUCCESS,'Your accoutn has been created !!')
    # messages.add_message(req,messages.INFO,' your information !!')
    # messages.add_message(req,messages.ERROR,'Your ERROR !!')
    # messages.add_message(req,messages.WARNING,'Last Warning !!')
    
    # message write secound method

    messages.success(req,'This is a Success !----')
    messages.info(req,'This is INFO ---->')
    messages.error(req,'This is a error --->')
    messages.warning(req,'This is Last warning ---!')
    messages.debug(req,'This is a debug--->')
    print(messages.get_level(req))
    # set debug value
    messages.set_level(req,messages.DEBUG)
    messages.debug(req,'This is a debug--->')


    return render(req,'app1/home.html')
def register(req):
    if req.method == 'POST':
        form=login(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Successfull Register')
    else:        
        form=login()
    return render(req,'app1/register.html',{'form':form})