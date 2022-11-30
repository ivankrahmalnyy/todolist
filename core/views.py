from django.contrib.auth import get_user_model, login, logout
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from core.serializers import RegistrationSerializer

USER_MODEL = get_user_model()


class RegistrationView(generics.CreateAPIView):
    model = USER_MODEL
    serializer_class = RegistrationSerializer


