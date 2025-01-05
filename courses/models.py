from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    max_students = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()