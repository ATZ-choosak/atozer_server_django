from django.urls import path
from .views import *


urlpatterns = [
    path("task_day_all/", TaskDayViewsetAll, name='task_day'),
    path("task_day/", TaskDayViewsetOne, name='task_day')
]
