from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "password")


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer Profile"""
    nik_name = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class CreateProfileSerializer(serializers.ModelSerializer):
    """Create profile"""

    class Meta:
        model = Profile
        fields = "__all__"
