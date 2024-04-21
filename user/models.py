import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from base.models import BaseModel
from user.managers import MyUserManager, MyUserGlobalManager


class User(AbstractUser, BaseModel):

    date_joined = None
    first_name = None
    last_name = None

    # username
    # password
    # email

    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    tg_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ForeignKey("UserPhotos", on_delete=models.SET_NULL, null=True, blank=True)

    objects = MyUserManager()
    global_objects = MyUserGlobalManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "Users"
        db_table = "auth_user"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("user", args=[str(self.id)])


def upload_user_photo(instance, filename):
    return f"user/photos/{instance.id}/{filename}"


class UserPhotos(BaseModel):

    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to=upload_user_photo)

    class Meta:
        verbose_name = "user photo"
        verbose_name_plural = "User photos"
        db_table = "user_photos"

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return reverse("user/photos", args=[str(self.id)])
