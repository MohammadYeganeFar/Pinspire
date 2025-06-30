from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    bio = models.CharField(max_length=255, null=True, blank=True)
    profile = models.ImageField(upload_to='user_profiles', null=True, blank=True)
    following = models.ManyToManyField('self',
                                    related_name='followers', 
                                    symmetrical=False,
                                    blank=True)

