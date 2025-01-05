from django.shortcuts import render, redirect, get_object_or_404
from .models import Course


def home(request):
    return render(request, 'index.html')

def course_list(request):
    courses = Course.objects.all()
    ctx = {'courses':courses}
    return render(request, 'courses/course-list.html', ctx)

def create_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        max_students = request.POST.get('max_students')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if name and description and duration and price and max_students and start_date and end_date:
            Course.objects.create(
                name = name,
                description = description,
                duration = duration,
                price = price,
                max_students = max_students,
                start_date = start_date,
                end_date = end_date
            )
            return redirect('courses:list')
    return render(request, 'courses/course-create.html')

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = course.students.all()
    ctx = {'course':course, 'students':students}
    return render(request, 'courses/course-detail.html', ctx)

def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses:list')
    ctx = {'course':course}
    return render(request, 'courses/course-delete-confirm.html', ctx)