from django.urls import path
from students import views

urlpatterns = [
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/create/', views.TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update/', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', views.TeacherDeleteView.as_view(), name='teacher_delete'),
    path('assignments/', views.TeacherSubjectAssignmentListView.as_view(), name='assignment_list'),
    path('assignments/create/', views.TeacherSubjectAssignmentCreateView.as_view(), name='assignment_create'),
    path('assignments/<int:pk>/update/', views.TeacherSubjectAssignmentUpdateView.as_view(), name='assignment_update'),
    path('assignments/<int:pk>/delete/', views.TeacherSubjectAssignmentDeleteView.as_view(), name='assignment_delete'),
]