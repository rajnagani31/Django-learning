from django.shortcuts import render
from .forms import studentregistration, teacherregistration
from django.http import HttpResponseRedirect
# Create your views here.


def student(request):
    if request.method == "POST":
        form = studentregistration(request.POST)
        if form.is_valid():
            form.save()
            

    else:
        form = studentregistration()

    return render(request, "app1/student.html", {"form": form})


def teacher(request):
    if request.method == "POST":
        form = teacherregistration(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = teacherregistration()
    return render(request, "app1/teacher.html", {"form": form})
