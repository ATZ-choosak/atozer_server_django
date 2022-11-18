from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework import serializers, viewsets


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class UsersViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Player.objects.all()
