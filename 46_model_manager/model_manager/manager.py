from django.db import models

class customModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all().order_by('-age')
    
class custommethod(models.Manager):
    def get_stu_age_range(self,r1,r2):
        return super().get_queryset().filter(age__range=(r1,r2)).order_by('age')    