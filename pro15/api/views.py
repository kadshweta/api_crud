from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    
   
# retrive delete update three at on code 
class StudentRList(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    
    