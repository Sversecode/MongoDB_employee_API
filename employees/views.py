from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404

#POST
class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#GET
class EmployeeDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "employee_id"

#UPDATE/PUT
class EmployeeUpdateView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employee_id'

    
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True   
        return super().update(request, *args, **kwargs)

#Delete
class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "employee_id"


#Aggregation 
from rest_framework.views import APIView

class EmployeeByDeptView(APIView):
    def get(self, request):
        dept = request.query_params.get("department")
        if not dept:
            return Response({"error": "Department query param required"}, status=400)
        employees = Employee.objects.filter(department=dept).order_by("-joining_date")
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


#Avg Salary
from django.db.models import Avg

class AvgSalaryView(APIView):
    def get(self, request):
        avg_salaries = Employee.objects.values("department").annotate(avg_salary=Avg("salary"))
        return Response(avg_salaries)

from django.db.models import Q
#Search by skill
class EmployeeSearchView(APIView):
    def get(self, request):
        skill = request.query_params.get("skill")
        if not skill:
            return Response({"error": "Skill query param required"}, status=400)
        employees = Employee.objects.filter(Q(skills__icontains=skill))

        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

