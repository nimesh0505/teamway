from django.db import models


class ShiftPeriodType(models.TextChoices):
    MORNING = "MORNING"
    AFTERNOON = "AFTERNOON"
    EVENING = "EVENING"
