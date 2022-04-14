from django.urls import path
from tracker.views import EmployeeView, EmployeeTrackerView

urlpatterns = [
    path(r"employee/", EmployeeView.as_view(), name="employee"),
    path(r"trackers/", EmployeeTrackerView.as_view(), name="tracker"),
]
