from django import forms

class login(forms.Form):
    Full_name=forms.CharField()

    email=forms.EmailField()

    password=forms.CharField(
        widget=forms.PasswordInput
    )