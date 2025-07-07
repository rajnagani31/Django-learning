from django.shortcuts import render
from app1.forms import Registration ,login
# Create your views here.
def Registrations(req):
    # fm=Registration()
    fm=Registration(field_order=['email','city'])
    
    return render(req,"app2/registration.html",{'form':fm})

def Login(req):
    # fm=login()
    # fm=login(auto_id='raj_%s')
    # fm=login(auto_id=False)
    # fm=login(auto_id=True)
    # fm=login(auto_id='raj')

    # fm=login(label_suffix='AB')

    fm=login(label_suffix='AB',initial={'email':"raj!123@gmail.com",'password':"neroraj214"},auto_id='raj_%s')
    return render(req,"app2/login.html",{'form':fm})


