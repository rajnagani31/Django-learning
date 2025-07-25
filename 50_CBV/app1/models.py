from django.db import models

# Create your models here.

class NeroTech(models.Model):
    name=models.CharField(max_length=100)
    age= models.IntegerField(blank=True,null=True)
    is_active=models.BooleanField(default=True)