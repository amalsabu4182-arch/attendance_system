from django import forms
from academics.models import Department, Classroom, Subject

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department Code'}),
        }

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'department', 'semester', 'section']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Classroom Name'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['code', 'name', 'classroom']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Code'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Name'}),
            'classroom': forms.Select(attrs={'class': 'form-control'}),
        }