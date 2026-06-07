from django.contrib import admin
from academics.models import Department, Classroom, Subject

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'created_at')
    search_fields = ('name', 'code')
    list_filter = ('created_at',)

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'semester', 'section', 'created_at')
    search_fields = ('name', 'department__name')
    list_filter = ('department', 'semester', 'section', 'created_at')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'classroom', 'created_at')
    search_fields = ('code', 'name', 'classroom__name')
    list_filter = ('classroom', 'created_at')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Subject, SubjectAdmin)