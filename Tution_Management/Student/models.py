# models.py

from django.db import models

class Student_models(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)  # Assuming student_id is the primary key
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_gender = models.CharField(max_length=10)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    paid_fee = models.DecimalField(max_digits=10, decimal_places=2)
