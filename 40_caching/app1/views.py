from django.shortcuts import render

# Create your views here.
def caching(request):

    return render (request,'app1/caching.html')