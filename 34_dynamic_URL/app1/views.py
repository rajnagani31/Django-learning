from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'app1/home.html')

# def profile(req,my_id):
#     student={'id':my_id}
#     return render(req,'app1/profile.html',student)


# def profile(req,my_class,my_id):
#     student={'my_class':my_class,'id':my_id}
#     return render(req,'app1/profile.html',student)

def profile(req,year):
    yr={'year':year}
    return render(req,'app1/profile.html',yr)
