from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    bio = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='user_profiles')
    following = models.ManyToManyField(self, through='Follow', related_name='followers', symmetrical=False

class Follow(models.Model):
    from_user = models.ForeignKey(CustomUser, 
                                                        on_delete=models.CASCADE, 
                                                        related_name='rel_from_set')
    to_user = models.ForeignKey(CustomUser, 
                                                        on_delete=models.CASCADE, 
                                                        related_name='rel_to_set')