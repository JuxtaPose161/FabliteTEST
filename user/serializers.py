from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()
class UsersForAdminSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "password",
                  "email", "is_active", "is_staff", "is_superuser",
                  "date_joined", "last_login", "groups", "user_permissions")
        read_only_fields = ("id", "date_joined", "last_login")
        extra_kwargs = {"password": {'write_only': True}}

class UsersForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "is_active", "is_staff")
        read_only_fields = ("is_active", "is_staff")