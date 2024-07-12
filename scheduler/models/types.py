from django.db import models

class DayChoices(models.TextChoices):
    MONDAY="monday", "monday"
    TUESDAY="tuesday", "tuesday"
    WEDNESDAY="wednesday", "wednesday"
    THURSDAY="thursday", "thursday"
    FRIDAY="friday", "friday"
    SATURDAY="saturday", "saturday"
    SUNDAY="sunday", "sunday"

