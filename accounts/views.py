from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import PasswordChangeView as DjangoPasswordChangeView
from django.contrib.auth.views import PasswordResetView as DjangoPasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView as DjangoPasswordResetConfirmView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import CustomUserCreationForm, UserProfileForm, CustomPasswordChangeForm
from accounts.models import CustomUser

User = get_user_model()

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Registration successful! Please log in.'

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name()}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    context = {'form': form}
    return render(request, 'accounts/profile.html', context)

class PasswordChangeView(SuccessMessageMixin, DjangoPasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('profile')
    success_message = 'Your password has been changed successfully!'

class PasswordResetView(SuccessMessageMixin, DjangoPasswordResetView):
    template_name = 'accounts/password_reset.html'
    success_url = reverse_lazy('password_reset_done')
    success_message = 'Check your email for password reset instructions.'

class PasswordResetConfirmView(SuccessMessageMixin, DjangoPasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('login')
    success_message = 'Your password has been reset successfully!'