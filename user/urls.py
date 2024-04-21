from django.urls import re_path

from user.views.destroy import UserDestroyAPIView
from user.views.update import UserUpdateAPIView
from user.views.list import UserListAPIView
from user.views.create import UserCreateAPIView

app = "user"

urlpatterns = [
    re_path(r"users/?", UserListAPIView.as_view(), name="list"),
    re_path(r"user/create/?", UserCreateAPIView.as_view(), name="create"),
    re_path(r"user/update/(?P<id>[0-9a-f-]+)/?", UserUpdateAPIView.as_view(), name="update"),
    re_path(r"user/delete/(?P<id>[0-9a-f-]+)/?", UserDestroyAPIView.as_view(), name="destroy"),
]
