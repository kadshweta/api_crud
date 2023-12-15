from django.contrib import admin
from .models import Student
# Register your models here go to seriallizer .
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
