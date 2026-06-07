from django.db import models
from students.models import Student
from academics.models import Subject
from accounts.models import CustomUser

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    period = models.IntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='present')
    marked_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('student', 'subject', 'date', 'period')
        ordering = ['-date']
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
    
    def __str__(self):
        return f"{self.student} - {self.subject} - {self.date}"

class AttendanceWarning(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='warnings')
    warning_type = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Attendance Warning'
        verbose_name_plural = 'Attendance Warnings'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.student} - {self.warning_type}"