from django.shortcuts import render
from .models import modelmanager
# Create your views here.
def table(request):
    all_data=[modelmanager.objects.all().get(pk=3)]

    all_data=modelmanager.objects.all()
    all_data=modelmanager.custom_manager.all()

    all_data=modelmanager.custom_method.get_stu_age_range(10,25)

    print(all_data)
    return render(request,'model_manager/manager.html',{'all_data':all_data})