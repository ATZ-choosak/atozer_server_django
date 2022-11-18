from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'players', UsersViewset, basename='users')

urlpatterns = router.urls
