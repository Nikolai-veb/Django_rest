from django.db import models
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Profile
from account.serializers import ProfileSerializer, CreateProfileSerializer


class ProfileView(generics.RetrieveAPIView):
    """Account"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateProfileView(generics.CreateAPIView):
    """"Create Account"""
    serializer_class = CreateProfileSerializer