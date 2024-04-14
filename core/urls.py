from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework_simplejwt.views import TokenObtainSlidingView

from core import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    re_path(r"token/?", TokenObtainSlidingView.as_view(), name="token_obtain_pair"),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
        re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    ]
