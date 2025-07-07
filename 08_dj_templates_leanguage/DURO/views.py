from django.shortcuts import render
from datetime import datetime
# Create your views here.
# Filter in html file
def django(request):
    name='DURO'
    Duration='3 month'
    work=f'{name} work ai based app and software provider for users use  in one place'
    con={
        'na':name,
        'du':Duration,
        'work':work,
    }
    return render(request,'DURO/dj.html',context=con)

# Date and Time

def date_time(request):
        d=datetime.now()
        return render(request,'DURO/date.html',context={'dt':d})

# FLOAT DATA

def float(request):
      p4=20.20+98.2233
      return render(request,'DURO/float.html',context={'p1':65.560,'p2':110.90922,'p3':238409732.932498732,'p4':p4})



# IF and ELSE TAG

def if_tag(request):
      
      return render(request,'DURO/if.html',context={'name':'Django','age':23})

# LOOP TAG

def loop(req):
    name={'names':['raj','dondo','ghelo','chiku','vidr','daglo']}
    complex_data={
          'stu1':{'name':'rahul','age':23},
          'stu2':{'name':'ghelo','age':213},
          'stu3':{'name':'daglo','age':13},

    }
    data={'studant':complex_data}
    return render (req,'DURO/loop.html', context=name)

# complec data Access

def complex(req):
    complex_data={
          'stu1':{'name':'rahul','age':23},
          'stu2':{'name':'ghelo','age':213},
          'stu3':{'name':'daglo','age':13},

    }
    data={'studant':complex_data}
    return render (req,'DURO/complex_data.html', context=data)