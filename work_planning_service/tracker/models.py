from django.db import models
from django.utils import timezone
from tracker.enums import ShiftPeriodType

from utils.utils import get_prefix_id


class Employee(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    employee_id = models.CharField(
        max_length=20, editable=False, help_text="ID exposed to end client"
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.employee_id = get_prefix_id("emp_")
        self.modified_at = timezone.now()
        return super(Employee, self).save(*args, **kwargs)


class EmployeeTracker(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    tracker_id = models.CharField(
        max_length=20, editable=False, help_text="ID exposed to end client"
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, blank=True, null=True
    )
    shift_period = models.CharField(
        max_length=20, choices=ShiftPeriodType.choices, default=ShiftPeriodType.MORNING
    )
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.tracker_id = get_prefix_id("trk_")
        self.modified_at = timezone.now()
        return super(EmployeeTracker, self).save(*args, **kwargs)
