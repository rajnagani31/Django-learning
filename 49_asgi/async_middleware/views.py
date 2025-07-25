from django.shortcuts import render

# Create your views here.
def sync_call(request):
    print("sync call yes")
    return render(request,'sync.html')


async def async_call(request):
    print("async call yes")
    return render(request,'async.html')