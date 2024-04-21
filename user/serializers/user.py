from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
            "groups": {"write_only": True},
            "user_permissions": {"write_only": True},
        }
