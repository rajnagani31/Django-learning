from django.shortcuts import render

# Create your views here.

def filter(request):
    data={'data':"hello everyone Today start a meeting at 8:00 pm on night ,today day is very good for all team memeber"}
    return render(request,'app1/creat_filter.html',context=data)
