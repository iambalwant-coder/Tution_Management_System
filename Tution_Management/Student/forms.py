from django import forms
from .models import Student_models

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student_models
        fields = '__all__'