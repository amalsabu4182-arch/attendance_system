from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
]