from django import forms
from .models import profile

class login(forms.ModelForm):

    confirm_password=forms.CharField()


    class Meta:
        model=profile
        # fields=['name','email','password']
        fields='__all__'
        labels={'name':"Full name","email":"your email id",'password':"your password"}
        error_messages={
            'email':{'required':'Email is required'},
            'password':{'required':'password is required'}
        }
        
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'write a name'}),
            'email':forms.TextInput(attrs={'placeholder':'write a Email'}),
            'password':forms.PasswordInput(attrs={'placeholder':'write a password'})

        }