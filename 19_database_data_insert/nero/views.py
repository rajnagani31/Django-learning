from django.shortcuts import render
from nero.models import Profile

def all(request):
    all_data=Profile.objects.all()
    con={'all_data':all_data}
    return render (request,"nero/all.html",context=con)


def single_data(request):
    single_data=Profile.objects.get(pk=1)
    return render (request,"nero/single.html",{'single_data':single_data})