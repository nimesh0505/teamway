from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from tracker.models import Employee, EmployeeTracker
from rest_framework import generics

from tracker.serializers import (
    EmployeeSerializer,
    EmployeeTrackerSerializer,
)


class EmployeeView(generics.CreateAPIView):
    quertset = Employee.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer
    http_method_names = ("post", "get")


class EmployeeTrackerView(generics.CreateAPIView):
    queryset = EmployeeTracker.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeTrackerSerializer
    http_method_names = (
        "post",
        "get",
    )
