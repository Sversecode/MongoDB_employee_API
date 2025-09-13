from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=50, unique=True)  
    name = models.CharField(max_length=100)                     
    department = models.CharField(max_length=100)               
    salary = models.FloatField()                                
    joining_date = models.CharField(max_length=20)                          
    skills = models.JSONField()                                 

    class Meta:
        db_table = "employees"   

    def __str__(self):
        return f"{self.employee_id} - {self.name}"