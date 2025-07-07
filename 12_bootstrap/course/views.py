from django.shortcuts import render

# Create your views here.
def learun_django(req):
    return render (req,"course/django.html")

def learun_python(req):
    return render (req,"course/pyhton.html")