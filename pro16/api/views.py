from django.shortcuts import render
from rest_framework.response import Response
from .models import Student 
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("**********list*********")
        print("basename:",self.basename)
        print("Action: ",self.action)
        print("Detail:",self.detail)
        print("Sufix:",self.suffix)
        print("name:",self.name)
        print("Description: ",self.description)
        stu=Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        print("**********retrive*********")
        print("basename:",self.basename)
        print("Action: ",self.action)
        print("Detail:",self.detail)
        print("Sufix:",self.suffix)
        print("name:",self.name)
        print("Description: ",self.description)
        id=pk 
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
    
    def Create(self,request):
        print("**********Create*********")
        print("basename:",self.basename)
        print("Action: ",self.action)
        print("Detail:",self.detail)
        print("Sufix:",self.suffix)
        print("name:",self.name)
        print("Description: ",self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

    def update(self,request,pk):
        print("**********Update*********")
        print("basename:",self.basename)
        print("Action: ",self.action)
        print("Detail:",self.detail)
        print("Sufix:",self.suffix)
        print("name:",self.name)
        print("Description: ",self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        print("**********partial Update*********")
        print("basename:",self.basename)
        print("Action: ",self.action)
        print("Detail:",self.detail)
        print("Sufix:",self.suffix)
        print("name:",self.name)
        print("Description: ",self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self,request,pk):
        print("**********partial Update*********")
        print("basename:",self.basename)
        print("Action: ",self.action)
        print("Detail:",self.detail)
        print("Sufix:",self.suffix)
        print("name:",self.name)
        print("Description: ",self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response ({'msg':'data deleted '})




    
    