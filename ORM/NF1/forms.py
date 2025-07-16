from .models import course_multi
from django import forms

class corseform(forms.Form):
    class Meta:
        model=course_multi
        field=['student_name','course_choice']

        widget={
            'course_choice':forms.MultipleChoiceField()
        }