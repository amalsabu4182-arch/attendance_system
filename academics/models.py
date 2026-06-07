from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Classroom(models.Model):
    SEMESTER_CHOICES = [
        (1, '1st Semester'),
        (2, '2nd Semester'),
        (3, '3rd Semester'),
        (4, '4th Semester'),
        (5, '5th Semester'),
        (6, '6th Semester'),
        (7, '7th Semester'),
        (8, '8th Semester'),
    ]
    
    SECTION_CHOICES = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('C', 'Section C'),
        ('D', 'Section D'),
    ]
    
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='classrooms')
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['department', 'semester', 'section']
        unique_together = ('department', 'semester', 'section')
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'
    
    def __str__(self):
        return f"{self.name} - Sem {self.semester} {self.section}"

class Subject(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='subjects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['code']
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        unique_together = ('code', 'classroom')
    
    def __str__(self):
        return f"{self.code} - {self.name}"