from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from user.models import User
from user.serializers.user import UserSerializer


class UserPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = "page_size"
    max_page_size = 100


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination

    def get_serializer_context(self):
        return {"request": self.request}
