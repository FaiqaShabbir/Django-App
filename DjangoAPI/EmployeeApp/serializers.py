# convert our complex Python objects into JSON format
from dataclasses import fields
from rest_framework import serializers
from EmployeeApp.models import Department, Employee

# serialize classes for both model
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('DepartmentId', 'DepartmentName')




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('EmployeeId', 'EmployeeName',
        'Department', 'DateOfJoining', 'PhotoFileName')
        