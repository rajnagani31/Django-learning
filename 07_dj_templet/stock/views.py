from django.shortcuts import render
from django.http import HttpResponse

def learn_django_in_stock(request):
    setes=100
    name={
        'cname':'nero',
        'st':setes
        }   #dynamic render 
    return render(request, 'stock/dj.html',context= name)

    # return HttpResponse("<h1>helloo<h1>")

def invest(req):
    return     HttpResponse("Invet in nero tech  !!")