from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.User):
    bio = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='user_profiles')
