from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class TweeterUser(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    location = models.CharField(max_length=200, null=True, blank=True)
    tweeter_user = models.OneToOneField(TweeterUser, on_delete=models.CASCADE, primary_key=True)
