from django.urls import path

from .views import *


urlpatterns = [
    path('task_week_all/', task_week_all),
    path('task_week/', task_week),
]
