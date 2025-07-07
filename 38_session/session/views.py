from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['fname']='raj'
    request.session['lname']='na'
    return render(request,'session/set_sessioon.html')

def get_session(request):
    name=request.session.get('fname')
    name_1=request.session.get('lname')

    return render(request,'session/get_session.html',{'id':name,'id_2':name_1})

def delete_session(request):
    if 'lname' in request.session:
        print('yes')
        del request.session['lname']
        # del request.session['lname']
    return render(request,'session/delete_session.html')

def flush_session(request):
    
    request.session.flush()# most case user to logout time becouse user data delete n browser and database
    # request.session.clear()
    return render(request,'session/flush_session.html')



