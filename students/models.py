from django.db import models
from accounts.models import CustomUser
from academics.models import Classroom

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    employee_id = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.employee_id})"

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    roll_number = models.CharField(max_length=50, unique=True)
    admission_number = models.CharField(max_length=50, unique=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='students')
    phone = models.CharField(max_length=15, blank=True)
    guardian_name = models.CharField(max_length=100, blank=True)
    guardian_phone = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.roll_number})"

class TeacherSubjectAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subject_assignments')
    subject = models.ForeignKey('academics.Subject', on_delete=models.CASCADE, related_name='teacher_assignments')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='teacher_assignments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('teacher', 'subject', 'classroom')
        verbose_name = 'Teacher-Subject Assignment'
        verbose_name_plural = 'Teacher-Subject Assignments'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.teacher} - {self.subject} ({self.classroom})"