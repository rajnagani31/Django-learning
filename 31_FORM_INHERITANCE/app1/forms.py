from django import forms
from .models import registartion


class studentregistration(forms.ModelForm):
    class Meta:
        model = registartion
        fields = ["student_name", "email", "password"]


class teacherregistration(studentregistration):
    class Meta(studentregistration.Meta):
        fields = ["teacher_name", "email", "password"]
