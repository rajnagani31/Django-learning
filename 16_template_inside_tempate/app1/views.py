from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,"app1/home.html")

def about(req):
    return render (req,'app1/about.html',{'name':'django'})