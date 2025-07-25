from django.http import HttpResponse
from django.shortcuts import render
from .models import manger


# Create your views here.
async def query_set(rquest):
    

    # async for i in  manger.objects.all():
    #     manager_data=(f"name : {i.name} age:{i.age} city:{i.city}")
    #     manager_data={'name':{i['name']}}

        # print(manager_data)

        count= await manger.objects.acount()
        print(count)

        async for i in manger.objects.filter(age__lt=22).aiterator():
                print(i.name)
        data = [await manger.objects.filter(age__lt=22).aiterator()]
        print(data)
        return HttpResponse('ok')    

# async def query_set(request):
#     # Use aiterator to fetch objects asynchronously
#     data = []

#     async for i in manger.objects.filter(age__lt=22).aiterator():
#         data.append(f"name: {i.name}, age: {i.age}, city: {i.city}")

#     return HttpResponse("<br>".join(data))