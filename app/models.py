from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import django
import datetime


class CustomUser(AbstractUser):
    user_type_data = ((1, "staff"), (2, "finance"), (3, "management"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class AdminManagement(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE, blank=True, null=True)
    address = models.TextField()
    nin = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
