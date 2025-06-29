from django.db import models
from core.models import Pin
from account.models import CustomUser


class Like(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE, related_name='likes')
    owner = models.ForeignKey(CustomUser,
                            on_delete=models.CASCADE, related_name='likes')
    

class Comment(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE, related_name='comments')
    owner = owner = models.ForeignKey(CustomUser,
                            on_delete=models.CASCADE, related_name='comments')
    
