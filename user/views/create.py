from rest_framework import generics
from rest_framework.response import Response

from user.serializers.create_user import UserCreateSerializer
from user.services.create import CreateUserService


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def get_queryset(self):
        return CreateUserService(
            username=self.request.data.get("username"),
            password=self.request.data.get("password")
        ).create()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        self.get_queryset()
        return Response({"ok": True})
