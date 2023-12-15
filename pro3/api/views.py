from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id = pydata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Student.object.all()
        serializer = StudentSerializer(stu, many=True)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        serializer =StudentSerializer(data=pydata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.error)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=="PUT":
        json_data=request.body 
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id = pydata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pydata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data cupdated !!! '}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=="DELETE":
        json_data=request.body 
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id = pydata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'data deleted  !!! '}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
       