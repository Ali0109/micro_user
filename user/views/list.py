from rest_framework import generics

from user.models import User
from user.paginations import UserPagination
from user.serializers.user import UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination

    def get_serializer_context(self):
        return {"request": self.request}
