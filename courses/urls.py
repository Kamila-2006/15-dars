from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('list/', views.course_list, name='list'),
    path('create/', views.create_course, name='create'),
    path('detail/<int:course_id>/', views.course_detail, name='detail'),
    path('delete/<int:course_id>/', views.course_delete, name='delete')
]