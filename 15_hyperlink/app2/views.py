from django.shortcuts import render

# Create your views here.
def django(request):
    return render(request,"app2/django.html")

def python(request):
    return render(request,"app2/python.html")