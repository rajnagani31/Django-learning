from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
def app1(request):
    return render (request,'app/app1.html')
@cache_page(30) # (30) or (timeout=30)
def app2(request):
    return render(request,'app/app2.html')

def app3(request):
    return render(request,'app/app3.html')