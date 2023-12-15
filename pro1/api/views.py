from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# model oject single student data 

def student_detail(request):
    # stu=Student.objects.get(id=pk)
    stu=Student.objects.all()
    #if you want fetch all data get replace with get() and many=true in serializer and usrl is single  
    serializer=StudentSerializer(stu,many=True) 
    json_data=JSONRenderer().render(serializer.data) 
    return HttpResponse(json_data,content_type='application/json')

# how can i see this data go tu url page