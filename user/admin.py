from django.contrib import admin

from user.models import User, UserPhotos


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "name", "email", "tg_id", "photo", "is_active", "created_at",)
    search_fields = ("username", "name",)
    list_filter = ("is_active",)
    ordering = ("created_at",)


@admin.register(UserPhotos)
class UserPhotosAdmin(admin.ModelAdmin):
    list_display = ("id", "photo", "created_at",)
    list_filter = ("is_active",)
    ordering = ("created_at",)

    @staticmethod
    def get_user_username(obj):
        return obj.user.username
