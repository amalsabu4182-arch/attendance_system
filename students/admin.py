from django.contrib import admin
from students.models import Student, Teacher, TeacherSubjectAssignment

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_number', 'classroom', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'roll_number')
    list_filter = ('classroom', 'created_at')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'phone', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'employee_id')
    list_filter = ('created_at',)

class TeacherSubjectAssignmentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'subject', 'classroom', 'created_at')
    search_fields = ('teacher__user__first_name', 'subject__name')
    list_filter = ('classroom', 'created_at')

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherSubjectAssignment, TeacherSubjectAssignmentAdmin)