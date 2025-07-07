from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def pin_lenght_validate(value):
    if len(str(value)) != 6:
        raise ValidationError('The PIN Code must be exactky 6 digits.')
stat_choice=(
    ('Andaman & Nicobar Island','Andaman & Nicobar Island'),
    ('Andhra pradesh','Andhra pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('chandigarh','chandigarh'),
    ('Dadar & Nagar Haveli','Dadar & Nagar Haveli'),
    ('Punjab','Punjab'),
    ('Rajasthan' ,'Rajasthan'),
    ('Gujrat','Gujrat'),
    ("Dehli",'Dehli'),

)    

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=1)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField(
        validators=[pin_lenght_validate],
        help_text='Enter 6-digit pin code'
    )
    state=models.CharField(choices=stat_choice,max_length=100)
    mobile=models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$')],
        help_text='Write 10 Digit Mobile number'
    )
    email=models.EmailField()
    job_city=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)