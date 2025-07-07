from django import forms
from .models import CK

class ckform(forms.ModelForm):
    class Meta:
        model=CK
        fields=['title','content']