from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ("password", "groups", "user_permissions")

    def get_photos(self, obj):
        request = self.context.get("request")
        user_photos = obj.photos.all()
        return [request.build_absolute_uri(photo.photo.url) for photo in user_photos]


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)
