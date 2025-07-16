from django.db import models
from django.contrib.auth.models import User



class Userprofile(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.PROTECT,limit_choices_to={'is_staff':False})
    # on_delete=models.Do_noting
    name=models.CharField(max_length=100)
    roll=models.IntegerField()

    # def __str__(self):
    #     return self.user
class Profile(models.Model):
    name=models.OneToOneField(Userprofile,on_delete=models.CASCADE)
    age=models.IntegerField()

class city(Profile):
    state=models.CharField(max_length=100)

    