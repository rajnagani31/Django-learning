from django import forms
from django.core import validators

import re
class form(forms.Form):
    def error_show(value):
        if value[0] != 'a':
            raise forms.ValidationError('please a enter first char "a"')
        
        if not value or not value[0].isupper():
            raise forms.ValidationError("Please enter a first letter capital")



    roll=forms.IntegerField(validators=[
        validators.MinValueValidator(101),
    ])
    name=forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(3)])
    email=forms.EmailField(validators=[error_show])
    choice=forms.ChoiceField(
        choices=[
            ('a','AI'),
            ('b',"ML"),
            ('c',"Blockchain")
        ],
        widget=forms.Select()
    )

    
