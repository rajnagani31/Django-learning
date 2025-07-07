from django.shortcuts import render
from app1.forms import demo,demo_update,demo_more_advance
# Create your views here.
def demo_(req):
    fm=demo()
    return render(req,'app1/demo.html',{'form':fm})

def demo_up(req):
    f=demo_update()
    return render(req,'app1/demo_up.html',{'form':f})

def demo_more_up(req):
    f=demo_more_advance()
    return render(req,'app1/demo_more_up.html',{'form':f})
 