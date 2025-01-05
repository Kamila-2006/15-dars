from django.db import models
from datetime import date


def today_date():
    return date.today()

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=14, unique=True)
    courses = models.ManyToManyField('courses.Course', related_name='students')
    notes = models.TextField()
    enrollment_date = models.DateField(default=today_date)