from django.urls import reverse
from django_dynamic_fixture import G
from utils.test_utils import get_access_token
from tracker.models import Employee
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from work_planning_service.tracker.enums import ShiftPeriodType
from work_planning_service.tracker.models import EmployeeTracker

client = APIClient()


class TestEmployeeTracker(APITestCase):
    def setUp(self) -> None:
        self.access_token = get_access_token()
        self.employee = G(Employee)
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)

    def test_add_employee_tracker(self):
        fixture = {
            "employee_id": self.employee.id,
            "shift_period": ShiftPeriodType.MORNING,
        }
        response = self.client.post(reverse("tracker", data=fixture, format="json"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_employee_tracker_twice_in_day(self):
        G(
            EmployeeTracker,
            employee=self.employee,
            shift_period=ShiftPeriodType.AFTERNOON,
        )
        fixture = {
            "employee_id": self.employee.id,
            "shift_period": ShiftPeriodType.MORNING,
        }
        response = self.client.post(reverse("tracker", data=fixture, format="json"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
