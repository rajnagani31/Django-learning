from django.shortcuts import render,redirect
from .forms import profileform
# Create your views here.
def home(req):
    if req.method == 'POST':
        fm=profileform(req.POST,req.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:    
        fm=profileform()
    return render(req,'app1/home.html',{'fm':fm})