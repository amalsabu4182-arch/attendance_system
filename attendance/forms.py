from django import forms
from attendance.models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'subject', 'date', 'period', 'status']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class BulkAttendanceForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'form-control'}))
    subject = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    period = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=Attendance.STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))