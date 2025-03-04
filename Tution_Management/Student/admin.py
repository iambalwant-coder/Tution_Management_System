from django.contrib import admin
from .models import Student_models

# Register your models here.


class Student_modelsAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_name', 'student_age', 'student_gender', 'total_fee', 'paid_fee')


admin.site.register(Student_models, Student_modelsAdmin)