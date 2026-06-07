from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from academics.models import Department, Classroom, Subject
from academics.forms import DepartmentForm, ClassroomForm, SubjectForm

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_admin()
    
    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to access this page.')
        return redirect('dashboard')

class DepartmentListView(AdminRequiredMixin, ListView):
    model = Department
    template_name = 'academics/department_list.html'
    context_object_name = 'departments'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Department.objects.all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search) | queryset.filter(code__icontains=search)
        return queryset

class DepartmentCreateView(AdminRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'academics/department_form.html'
    success_url = reverse_lazy('department_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Department created successfully!')
        return super().form_valid(form)

class DepartmentUpdateView(AdminRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'academics/department_form.html'
    success_url = reverse_lazy('department_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Department updated successfully!')
        return super().form_valid(form)

class DepartmentDeleteView(AdminRequiredMixin, DeleteView):
    model = Department
    template_name = 'academics/confirm_delete.html'
    success_url = reverse_lazy('department_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Department deleted successfully!')
        return super().delete(request, *args, **kwargs)

class ClassroomListView(AdminRequiredMixin, ListView):
    model = Classroom
    template_name = 'academics/classroom_list.html'
    context_object_name = 'classrooms'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Classroom.objects.all().select_related('department')
        search = self.request.GET.get('search')
        department_filter = self.request.GET.get('department')
        
        if search:
            queryset = queryset.filter(name__icontains=search)
        if department_filter:
            queryset = queryset.filter(department_id=department_filter)
        
        return queryset

class ClassroomCreateView(AdminRequiredMixin, CreateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'academics/classroom_form.html'
    success_url = reverse_lazy('classroom_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Classroom created successfully!')
        return super().form_valid(form)

class ClassroomUpdateView(AdminRequiredMixin, UpdateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'academics/classroom_form.html'
    success_url = reverse_lazy('classroom_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Classroom updated successfully!')
        return super().form_valid(form)

class ClassroomDeleteView(AdminRequiredMixin, DeleteView):
    model = Classroom
    template_name = 'academics/confirm_delete.html'
    success_url = reverse_lazy('classroom_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Classroom deleted successfully!')
        return super().delete(request, *args, **kwargs)

class SubjectListView(AdminRequiredMixin, ListView):
    model = Subject
    template_name = 'academics/subject_list.html'
    context_object_name = 'subjects'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Subject.objects.all().select_related('classroom')
        search = self.request.GET.get('search')
        classroom_filter = self.request.GET.get('classroom')
        
        if search:
            queryset = queryset.filter(name__icontains=search) | queryset.filter(code__icontains=search)
        if classroom_filter:
            queryset = queryset.filter(classroom_id=classroom_filter)
        
        return queryset

class SubjectCreateView(AdminRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'academics/subject_form.html'
    success_url = reverse_lazy('subject_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Subject created successfully!')
        return super().form_valid(form)

class SubjectUpdateView(AdminRequiredMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'academics/subject_form.html'
    success_url = reverse_lazy('subject_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Subject updated successfully!')
        return super().form_valid(form)

class SubjectDeleteView(AdminRequiredMixin, DeleteView):
    model = Subject
    template_name = 'academics/confirm_delete.html'
    success_url = reverse_lazy('subject_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Subject deleted successfully!')
        return super().delete(request, *args, **kwargs)