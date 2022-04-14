from department.models import Department, Employee
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, generics
from rest_framework.pagination import PageNumberPagination
from .serializers import EmployeeSerializer, DepartmentSerializer


class EmployeeViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class EmployeeViewSet(viewsets.ModelViewSet):
    """Allows to filter query by last_name and department id"""
    queryset = Employee.objects.all().prefetch_related()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated,]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('last_name', 'department')
    pagination_class = EmployeeViewSetPagination


class DepartmentListView(generics.ListAPIView):
    """Returns all departments"""
    queryset = Department.objects.all().prefetch_related()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny,]

