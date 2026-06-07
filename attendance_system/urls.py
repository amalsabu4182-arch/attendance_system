from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('attendance/', include('attendance.urls')),
    path('reports/', include('reports.urls')),
    path('students/', include('students.urls')),
    path('academics/', include('academics.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Attendance Management System"
admin.site.site_title = "AMS Admin"
admin.site.index_title = "Welcome to Attendance Management System"