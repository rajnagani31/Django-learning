from django import forms
from .models import profile

GENDER_CHOICE={
    ('f','Femail'),
    ('M',"Mail"),
    ("O",'Other'),
}

JOB_CITY=[
    ('Delhi',"Delhi"),
    ('Surat',"Surat"),
    ('Pune','Pune'),
    ('Bangluru','Bangluru'),
    ('Mumbai','Mumbai')
]
class profileform(forms.ModelForm):
    gender=forms.ChoiceField(
        choices=GENDER_CHOICE,
        widget=forms.RadioSelect,
    )
    job_city=forms.MultipleChoiceField(
        choices=JOB_CITY,
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model=profile
        fields=[
            'name','dob','gender','locality','city','pin','state','mobile','email','job_city',"profile_image",'my_file'
        ]
        labels={
            'name':'Full name',
            'dob':'Date of Birth'
        }
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Write Full Name','class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker','type':'date'}),
            'locality':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a area'}),
            'city':forms.TextInput(attrs={'calss':'form-control','placeholder':'city'}),
            'pin':forms.NumberInput(attrs={'class':'form-control','placeholder':'6-digit pin'}),
            'state':forms.Select(attrs={'calss':'form-control'}),
            'mobile':forms.TextInput(attrs={'calss':'form-control'}),
            'email':forms.EmailInput(attrs={'calss':'form-control','placeholder':'Email Address'}),



        }