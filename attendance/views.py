from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from attendance.models import Attendance
from students.models import Student
from academics.models import Subject, Classroom
from attendance.forms import AttendanceForm

class TeacherRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_teacher() or self.request.user.is_admin()
    
    def handle_no_permission(self):
        messages.error(self.request, 'Access denied')
        return redirect('dashboard')

@login_required
def mark_attendance(request):
    if not (request.user.is_teacher() or request.user.is_admin()):
        messages.error(request, 'Access denied')
        return redirect('dashboard')
    
    if request.method == 'POST':
        classroom_id = request.POST.get('classroom')
        subject_id = request.POST.get('subject')
        date = request.POST.get('date')
        period = request.POST.get('period')
        
        classroom = get_object_or_404(Classroom, id=classroom_id)
        subject = get_object_or_404(Subject, id=subject_id)
        
        students = Student.objects.filter(classroom=classroom)
        
        for student in students:
            status = request.POST.get(f'status_{student.id}', 'absent')
            Attendance.objects.update_or_create(
                student=student,
                subject=subject,
                date=date,
                period=period,
                defaults={'status': status, 'marked_by': request.user}
            )
        
        messages.success(request, 'Attendance marked successfully!')
        return redirect('mark_attendance')
    
    classrooms = Classroom.objects.all()
    subjects = Subject.objects.all()
    
    context = {
        'classrooms': classrooms,
        'subjects': subjects,
    }
    
    return render(request, 'attendance/mark_attendance.html', context)

class AttendanceListView(TeacherRequiredMixin, ListView):
    model = Attendance
    template_name = 'attendance/attendance_list.html'
    context_object_name = 'attendance_records'
    paginate_by = 20
    
    def get_queryset(self):
        return Attendance.objects.select_related('student', 'subject')

class AttendanceUpdateView(TeacherRequiredMixin, UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'attendance/attendance_form.html'
    success_url = reverse_lazy('attendance_list')

class AttendanceDeleteView(TeacherRequiredMixin, DeleteView):
    model = Attendance
    template_name = 'attendance/confirm_delete.html'
    success_url = reverse_lazy('attendance_list')