from django.contrib import admin
from attendance.models import Attendance, AttendanceWarning

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'date', 'period', 'status', 'marked_by', 'created_at')
    search_fields = ('student__user__first_name', 'subject__name')
    list_filter = ('status', 'date', 'subject', 'created_at')
    date_hierarchy = 'date'

class AttendanceWarningAdmin(admin.ModelAdmin):
    list_display = ('student', 'warning_type', 'is_resolved', 'created_at')
    search_fields = ('student__user__first_name', 'warning_type')
    list_filter = ('warning_type', 'is_resolved', 'created_at')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceWarning, AttendanceWarningAdmin)