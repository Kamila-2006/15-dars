from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('list/', views.students_list, name='list'),
    path('create/', views.create_student, name='create'),
    path('detail/<int:student_id>/', views.student_detail, name='detail'),
    path('delete/<int:student_id>/', views.student_delete, name='delete'),
    path('update/<int:student_id>/', views.edit_profile, name='update')
]