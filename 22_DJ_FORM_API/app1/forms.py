from django import forms

class Registration(forms.Form):
    First_name=forms.CharField()
    Last_name=forms.CharField()
    email=forms.EmailField()
    city=forms.CharField()
    
class login(forms.Form):
    email=forms.EmailField()
    password=forms.CharField()