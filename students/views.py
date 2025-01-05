from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from courses.models import Course


def students_list(request):
    students = Student.objects.all()
    ctx = {'students':students}
    return render(request, 'students/student-list.html', ctx)

def create_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        course_ids = request.POST.getlist('courses')
        notes = request.POST.get('notes')
        if first_name and last_name and email and phone_number and notes:
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                notes=notes
            )
            if course_ids:
                courses = Course.objects.filter(id__in=course_ids)
                student.courses.set(courses)
            return redirect('students:list')
    courses = Course.objects.all()
    ctx = {'courses':courses}
    return render(request, 'students/student-create.html', ctx)

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses = student.courses.all()
    ctx = {'student':student, 'courses':courses}
    return render(request, 'students/student-detail.html', ctx)

def edit_profile(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        course_ids = request.POST.getlist('courses')
        notes = request.POST.get('notes')
        if first_name and last_name and email and phone_number and notes:
            student.first_name = first_name
            student.last_name = last_name
            student.email = email
            student.phone_number = phone_number
            student.notes = notes
            if course_ids:
                courses = Course.objects.filter(id__in=course_ids)
                student.courses.set(courses)
            student.save()
            return redirect('students:detail', student.id)
    courses = Course.objects.all()
    ctx = {'student':student, 'courses':courses}
    return render(request, 'students/student-create.html', ctx)

def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('students:list')
    ctx = {'student':student}
    return render(request, 'students/student-delete-confirm.html', ctx)