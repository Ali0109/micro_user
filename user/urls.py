from django.urls import re_path

from user.views.destroy import UserDestroyAPIView
from user.views.notification import UserNotificationAPIView
from user.views.update import UserUpdateAPIView
from user.views.list import UserListAPIView
from user.views.create import UserCreateAPIView

app = "user"

urlpatterns = [
    re_path(r"list/?", UserListAPIView.as_view(), name="list"),
    re_path(r"create/?", UserCreateAPIView.as_view(), name="create"),
    re_path(r"update/(?P<id>[0-9a-f-]+)/?", UserUpdateAPIView.as_view(), name="update"),
    re_path(r"destroy/(?P<id>[0-9a-f-]+)/?", UserDestroyAPIView.as_view(), name="destroy"),
    re_path(r"notification/?", UserNotificationAPIView.as_view(), name="notification"),
]
