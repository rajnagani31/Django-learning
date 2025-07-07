from django.db import models
from django_ckeditor import CKEditor5Field
# Create your models here.

class CK(models.Model):
    title=models.CharField(max_length=200)
    content=CKEditor('Text', config_name='extends')
