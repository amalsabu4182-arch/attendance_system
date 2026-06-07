from django.urls import path
from reports import views

urlpatterns = [
    path('student/', views.student_attendance_report, name='student_report'),
]