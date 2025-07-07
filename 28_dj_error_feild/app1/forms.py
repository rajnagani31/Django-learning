from django import forms

class user_login(forms.Form):
    name=forms.CharField(error_messages={"required":"Name is required"})
    email=forms.EmailField(error_messages={'required':"Email is required"},min_length=5,max_length=20)
    password=forms.CharField(
        error_messages={'required':"Password is required"},
        widget=forms.PasswordInput
        ) 

