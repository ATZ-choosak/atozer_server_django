from django.db import models
from users.models import Player


class Task_week(models.Model):
    users = models.ManyToManyField(Player, related_name="users")
    status_1 = models.BooleanField(default=False, blank=True, null=True)
    status_2 = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return ":".join([a.name for a in self.users.all()]) + "-" + str(self.date)
