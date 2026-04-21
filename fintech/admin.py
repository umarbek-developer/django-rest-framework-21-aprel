from django.contrib import admin
from .models import Teacher, Student, Group 
# Register your models here.

# admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(Group)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "specialization")
    search_fields = ("first_name", "last_name", "email", "specialization")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "yosh", "last_name", "group", "enrollment_date")
    search_fields = ("first_name", "last_name", "group__name")
    list_filter = ("group", "enrollment_date")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "created_at")
