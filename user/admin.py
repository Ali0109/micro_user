from django.contrib import admin

from user.models import User, UserPhotos


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "name", "email", "tg_id", "is_active", "created_at",)
    search_fields = ("username", "name",)
    list_filter = ("is_active",)


@admin.register(UserPhotos)
class UserPhotosAdmin(admin.ModelAdmin):
    list_display = ("id", "get_user_username", "photo", "created_at",)
    search_fields = ("user__username",)
    list_filter = ("is_active",)

    @staticmethod
    def get_user_username(obj):
        return obj.user.username
