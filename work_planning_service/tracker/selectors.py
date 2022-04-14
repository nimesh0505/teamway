from datetime import date
from typing import Optional

from tracker.models import EmployeeTracker


def get_employee_tracker_by_id_and_date(
    employee_id: int, work_date: date
) -> Optional[EmployeeTracker]:
    return EmployeeTracker.objects.filter(
        employee_id=employee_id, created_at=work_date
    ).first()
