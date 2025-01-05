# Generated by Django 5.1.4 on 2025-01-05 11:17

import students.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=14, unique=True)),
                ('notes', models.TextField()),
                ('enrollment_date', models.DateField(default=students.models.today_date)),
                ('courses', models.ManyToManyField(related_name='students', to='courses.course')),
            ],
        ),
    ]
