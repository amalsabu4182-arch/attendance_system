from django.urls import path
from attendance import views

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('', views.AttendanceListView.as_view(), name='attendance_list'),
    path('<int:pk>/edit/', views.AttendanceUpdateView.as_view(), name='attendance_edit'),
    path('<int:pk>/delete/', views.AttendanceDeleteView.as_view(), name='attendance_delete'),
]