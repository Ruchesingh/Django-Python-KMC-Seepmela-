from django.contrib import admin

from home.models import Student, StudentProfile

# Register your models here.
#admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','dob','number']
    search_fields=['name','dob']
    list_filter=['is_active','name']


@admin.register(StudentProfile)
class StudetProfileAdmin(admin.ModelAdmin):
    list_display = ['student','address','email']