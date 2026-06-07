from django import forms
from students.models import Teacher, Student, TeacherSubjectAssignment

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['employee_id', 'phone', 'qualification']
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_number', 'admission_number', 'classroom', 'phone', 'guardian_name', 'guardian_phone']
        widgets = {
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'admission_number': forms.TextInput(attrs={'class': 'form-control'}),
            'classroom': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TeacherSubjectAssignmentForm(forms.ModelForm):
    class Meta:
        model = TeacherSubjectAssignment
        fields = ['teacher', 'subject', 'classroom']
        widgets = {
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'classroom': forms.Select(attrs={'class': 'form-control'}),
        }