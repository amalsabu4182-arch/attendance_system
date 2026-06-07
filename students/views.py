from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from students.models import Student, Teacher, TeacherSubjectAssignment
from students.forms import StudentForm, TeacherForm, TeacherSubjectAssignmentForm

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_admin()
    
    def handle_no_permission(self):
        messages.error(self.request, 'Access denied')
        return redirect('dashboard')

class StudentListView(AdminRequiredMixin, ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Student.objects.select_related('user', 'classroom')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(user__first_name__icontains=search) | \
                      queryset.filter(user__last_name__icontains=search) | \
                      queryset.filter(roll_number__icontains=search)
        return queryset

class StudentCreateView(AdminRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(AdminRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(AdminRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/confirm_delete.html'
    success_url = reverse_lazy('student_list')

class TeacherListView(AdminRequiredMixin, ListView):
    model = Teacher
    template_name = 'students/teacher_list.html'
    context_object_name = 'teachers'
    paginate_by = 10
    
    def get_queryset(self):
        return Teacher.objects.select_related('user')

class TeacherCreateView(AdminRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'students/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherUpdateView(AdminRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'students/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherDeleteView(AdminRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'students/confirm_delete.html'
    success_url = reverse_lazy('teacher_list')

class TeacherSubjectAssignmentListView(AdminRequiredMixin, ListView):
    model = TeacherSubjectAssignment
    template_name = 'students/assignment_list.html'
    context_object_name = 'assignments'
    paginate_by = 10

class TeacherSubjectAssignmentCreateView(AdminRequiredMixin, CreateView):
    model = TeacherSubjectAssignment
    form_class = TeacherSubjectAssignmentForm
    template_name = 'students/assignment_form.html'
    success_url = reverse_lazy('assignment_list')

class TeacherSubjectAssignmentUpdateView(AdminRequiredMixin, UpdateView):
    model = TeacherSubjectAssignment
    form_class = TeacherSubjectAssignmentForm
    template_name = 'students/assignment_form.html'
    success_url = reverse_lazy('assignment_list')

class TeacherSubjectAssignmentDeleteView(AdminRequiredMixin, DeleteView):
    model = TeacherSubjectAssignment
    template_name = 'students/confirm_delete.html'
    success_url = reverse_lazy('assignment_list')