from datetime import datetime
from django.forms import ValidationError
from rest_framework import serializers

from tracker.models import Employee, EmployeeTracker
from tracker.selectors import get_employee_tracker_by_id_and_date

import logging

logger = logging.getLogger(__name__)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTracker
        fields = "__all__"

    def create(self, validated_data):
        employee_id = validated_data["employee_id"]
        if work_info := get_employee_tracker_by_id_and_date(
            employee_id=employee_id, work_date=datetime.date.today()
        ):
            logger.warning(
                f"The employee {employee_id} has already worked on {work_info.shift_period}"
            )
            raise ValidationError(
                f"The employee {employee_id} cannot have two shifts on the same day"
            )
        return super().create(validated_data)
