from django.shortcuts import render
from django.http import HttpResponse
from .models import city

def city_data(request):
    data=city.objects.get(id=7)

    print(data.state)
    print(data.age)
    print(data.name.name)
    print(data.name.roll)
    print(data.name.user)
    return HttpResponse('complete')