from email.policy import default
from django.db import models
from users.models import Player


class Task_day(models.Model):
    users = models.ForeignKey(
        Player, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return F"{self.users.name} : {self.date}"
