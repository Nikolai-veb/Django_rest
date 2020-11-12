from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    """Serializer Profile"""
    nik_name = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class CreateProfileSerializer(serializers.ModelSerializer):
    """Create profile"""
    first_name = serializers.SlugRelatedField(slug_field="first_name", read_only=True)
    last_name = serializers.SlugRelatedField(slug_field='last_name', read_only=True)
    password = serializers.SlugRelatedField(slug_field='password', read_only=True)

    class Meta:
        model = Profile
        fields = ("nik_name", "email", "date_birth", "photo", "password", "first_name", "last_name")
