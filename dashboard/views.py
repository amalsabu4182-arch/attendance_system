from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from students.models import Student, Teacher
from academics.models import Department, Classroom, Subject
from attendance.models import Attendance

@login_required
def dashboard(request):
    user = request.user
    
    if user.is_admin():
        return admin_dashboard(request)
    elif user.is_teacher():
        return teacher_dashboard(request)
    elif user.is_student():
        return student_dashboard(request)
    else:
        return redirect('login')

def admin_dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_subjects = Subject.objects.count()
    total_classrooms = Classroom.objects.count()
    total_departments = Department.objects.count()
    
    today = datetime.now().date()
    today_attendance = Attendance.objects.filter(date=today, status='present').count()
    today_total = Attendance.objects.filter(date=today).count()
    today_percentage = (today_attendance / today_total * 100) if today_total > 0 else 0
    
    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_subjects': total_subjects,
        'total_classrooms': total_classrooms,
        'total_departments': total_departments,
        'today_percentage': f"{today_percentage:.2f}",
    }
    
    return render(request, 'dashboard/admin_dashboard.html', context)

def teacher_dashboard(request):
    teacher = request.user.teacher_profile if hasattr(request.user, 'teacher_profile') else None
    today = datetime.now().date()
    
    today_classes = Attendance.objects.filter(
        date=today,
        marked_by=request.user
    ).values('subject', 'period').distinct().count()
    
    context = {
        'teacher': teacher,
        'today_classes': today_classes,
    }
    
    return render(request, 'dashboard/teacher_dashboard.html', context)

def student_dashboard(request):
    student = request.user.student_profile if hasattr(request.user, 'student_profile') else None
    
    if not student:
        return redirect('login')
    
    context = {
        'student': student,
    }
    
    return render(request, 'dashboard/student_dashboard.html', context)