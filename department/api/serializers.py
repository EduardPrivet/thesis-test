from department.models import Employee, Department
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField()
    salary_sum = serializers.SerializerMethodField()

    def get_employee_count(self, obj):
        return obj.employees.all().count()

    def get_salary_sum(self, obj):
        return sum([employee.salary for employee in obj.employees.all()])

    class Meta:
        fields = "__all__"
        model = Department


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Employee

