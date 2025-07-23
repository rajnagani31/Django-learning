from django.http import JsonResponse
from django.shortcuts import render
from asgiref.sync import sync_to_async,async_to_sync
from .models import Student
# Create your views here.

# synchorouns to asynchronous function
def data_sync(x):
    return x ** 2

async def deta_call_async():
    ans=await sync_to_async(data_sync)(5)
    print(ans)
    
#  Asynchronous to synchronous function

async def my_data(x):
    await None
    return x ** 3

def coll_my_data():
    async_to_sync(my_data)(5)

# ORM using sunc to asyncs

def get_data():
    return list(Student.objects.all().values())

async def call_get_data(request):
    data = await sync_to_async(lambda :list(Student.objects.all().values()))()
    
    return JsonResponse({'data':data})