from rest_framework import serializers
from .models import Student


# model serializer 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=['name','roll','city']
        # extra_kwargs={'name':{'read_only':True}}
