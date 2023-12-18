from django.contrib import admin
from .models import Student
# Register your models/table here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']