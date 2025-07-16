from django import forms 

class registration(forms.Form):
    First_name=forms.CharField(help_text='Write yor first name')
    last_name=forms.CharField(initial="Nagani")
    Email=forms.EmailField()


class address(forms.Form):
    name=forms.CharField()
    city=forms.CharField()
    state=forms.CharField()
    pin_code=forms.CharField()

class Login(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    key=forms.CharField(widget=forms.HiddenInput())    

