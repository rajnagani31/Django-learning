from django.shortcuts import render
from django.http import JsonResponse
import time
import uvicorn
import httpx, asyncio

# Create your views here.
def sync_function(request):
    start_time=time.time()
    responses=[]
    for _ in range(5):
        response=httpx.get('https://jsonplaceholder.typicode.com/posts')
        responses.append(response.json())
    end_time=time.time()
    time_taken=end_time-start_time
    return JsonResponse({
        "status" : "Success",
        "Time": f"{time_taken:.2f} secounds",
        "data": 5

    })
async def async_function_view(request):
    start_time=time.time()

    async with httpx.AsyncClient() as Client:
        tasks = [Client.get('https://jsonplaceholder.typicode.com/posts') for _ in range(5)]
        responses= await asyncio.gather(*tasks)

    end_time=time.time()

    time_taken= end_time - start_time
    return JsonResponse({
        'status ': "success",
        "time" : f"{time_taken} secounds",
        "data" : 5
    })    

def sync_func(request):
    start_time=time.time()
    for _ in range(1000):
            response=httpx.get("https://jsonplaceholder.typicode.com/posts")

    end_time=time.time()
    teak_time=end_time-start_time
    return JsonResponse({
         'data':20,
         'Time':f"{teak_time} secounds"
    })        

semaphore = asyncio.Semaphore(1000)
async def fetch(client, url):
    async with semaphore:
        response = await client.get(url)
        return response
    
async def async_func(request):
    start_time=time.time()
    url="https://jsonplaceholder.typicode.com/posts"
    async with httpx.AsyncClient() as client:
        tasks= [fetch(client,url) for _ in range(1000)]
        data=await asyncio.gather(*tasks, return_exceptions=True)
    end_time=time.time()
    teak_time=end_time-start_time


    return JsonResponse({
         "data" : len(data),
         "Time":f"{teak_time} secounds"
    })
        