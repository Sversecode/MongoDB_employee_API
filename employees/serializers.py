from rest_framework import serializers
from .models import Employee
import re

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee                  # link this serializer to the Employee model
        fields = "__all__"                # include all model fields

    # Extra validation for salary
    def validate_salary(self, value):
        if value < 0:
            raise serializers.ValidationError("Salary must be non-negative")
        return value

    def validate_joining_date(self, value):
        # validate format: YYYY-MM-DD
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', value):
            raise serializers.ValidationError("Joining date must be in YYYY-MM-DD format")
        return value