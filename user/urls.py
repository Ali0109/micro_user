from django.urls import re_path

from user.views.list import UserListAPIView
from user.views.create import UserCreateAPIView

app = "user"

urlpatterns = [
    re_path(r"list/?", UserListAPIView.as_view(), name="list"),
    re_path(r"create/?", UserCreateAPIView.as_view(), name="create"),
]
