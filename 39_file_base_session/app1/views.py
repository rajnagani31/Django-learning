from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['fname'] = 'raj'
    request.session['lname'] = 'nagsani'

    return render(request,'app1/set.html')

def get_session(request):
    first_name=request.session.get('fname')
    last_name=request.session.get('lname')

    return render(request,'app1/get.html',{'fname':first_name,'lname':last_name})

def delete_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'app1/delete.html')