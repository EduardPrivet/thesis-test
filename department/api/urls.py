from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api_department"
router = routers.SimpleRouter()
router.register('employee', views.EmployeeViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('department/', views.DepartmentListView.as_view(), name='department')
]