from django.db import models
from django.contrib.auth.models import AbstractUser
from .user_manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Site(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
