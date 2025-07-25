from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import NeroTech
import asyncio
# Create your views here.
class Myclass(ListView):
    model= NeroTech
    name='raj'
    def get(self,request):
        # data = NeroTech.objects.all()
        data =  self.get_queryset().all().filter(age=20)
        print(data)
        return HttpResponse(self.name)
        
class AsyncView(View):
    async def get(self,request ,*args , **kwargs):
        await asyncio.sleep(3)
        return HttpResponse('okey')
            

# TemplateView              

