from django.urls import path
from academics import views

urlpatterns = [
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/create/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),
    path('classrooms/', views.ClassroomListView.as_view(), name='classroom_list'),
    path('classrooms/create/', views.ClassroomCreateView.as_view(), name='classroom_create'),
    path('classrooms/<int:pk>/update/', views.ClassroomUpdateView.as_view(), name='classroom_update'),
    path('classrooms/<int:pk>/delete/', views.ClassroomDeleteView.as_view(), name='classroom_delete'),
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/create/', views.SubjectCreateView.as_view(), name='subject_create'),
    path('subjects/<int:pk>/update/', views.SubjectUpdateView.as_view(), name='subject_update'),
    path('subjects/<int:pk>/delete/', views.SubjectDeleteView.as_view(), name='subject_delete'),
]