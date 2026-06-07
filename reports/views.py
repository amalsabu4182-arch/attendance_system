from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from attendance.models import Attendance
from students.models import Student

def calculate_attendance_percentage(student, subject=None):
    query = Attendance.objects.filter(student=student)
    if subject:
        query = query.filter(subject=subject)
    
    total = query.count()
    if total == 0:
        return 0
    
    present = query.filter(status='present').count()
    return (present / total) * 100

@login_required
def student_attendance_report(request):
    if not (request.user.is_admin() or request.user.is_teacher()):
        messages.error(request, 'Access denied')
        return redirect('dashboard')
    
    students = Student.objects.all()
    report_data = []
    
    for student in students:
        attendance_pct = calculate_attendance_percentage(student)
        report_data.append({
            'student': student,
            'attendance_percentage': attendance_pct,
        })
    
    context = {'report_data': report_data}
    return render(request, 'reports/student_report.html', context)