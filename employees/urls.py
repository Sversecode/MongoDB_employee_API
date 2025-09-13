from django.urls import path
from .views import (
    EmployeeCreateView,
    EmployeeDetailView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeByDeptView,
    AvgSalaryView,
    EmployeeSearchView
)

urlpatterns = [
    path("employees", EmployeeCreateView.as_view()),                    
    path("employees/<str:employee_id>", EmployeeDetailView.as_view()),  
    path("employees/<str:employee_id>/update", EmployeeUpdateView.as_view()),  
    path("employees/<str:employee_id>/delete", EmployeeDeleteView.as_view()),  
    path("employees/by-department/", EmployeeByDeptView.as_view()),      
    path("employees/avg-salary/", AvgSalaryView.as_view()),              
    path("employees/search/", EmployeeSearchView.as_view()),       
]
