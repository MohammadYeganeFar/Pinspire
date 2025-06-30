from django.db import models


class Pin(models.Model):
    PRIVATE = 'PR'
    PUBLIC = 'PU'
    visibility_choices = {
        PRIVATE: 'Private',
        PUBLIC: 'Public'
    }
    image = models.ImageField(upload_to='pins_images', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=150, null=True, blank=True)
    visibility = models.CharField(max_length=2, choices=visibility_choices)


class Board(models.Model):
    PRIVATE = 'PR'
    PUBLIC = 'PU'
    visibility_choices = {
        PRIVATE: 'Private',
        PUBLIC: 'Public'
    }
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    visibility = models.CharField(max_length=2, choices=visibility_choices)
    