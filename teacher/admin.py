from django.contrib import admin

from teacher.models import Grade, Teacher

# Register your models here.
#admin.site.register(Grade)
#admin.site.register(Teacher)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['name','section','created_at','updated_at']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['grade','name','age']