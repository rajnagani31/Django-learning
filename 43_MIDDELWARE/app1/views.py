from django.shortcuts import render
from django.http import Http404
from django.template.response import TemplateResponse


# Create your views here.
def home(request):
    print("I am home")
    # raise Http404("Task not found")
    return render(request, "app1/home.html")


def math(request):
    a = 10
    b = 90
    c = a + b / 3
    print("I am math")
    return render(request, "app1/math.html", {"a": c})


def user(request):
    print("I am user")
    return render(request, "app1/user.html")


def name(request):
    print("I am user info")
    context = {"name": "raj"}
    return TemplateResponse(request, "app1/name.html", context)
