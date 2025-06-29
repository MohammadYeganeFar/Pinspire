from django.db import models


class Pin(models.Model):
    PRIVATE = 'PR'
    PUBLIC = 'PU'
    visibility_choices = {
        PRIVATE: 'Private',
        PUBLIC: 'Public'
    }
    image = models.ImageField(upload_to='pins_images')
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=150)
    visibility = models.CharField(max_length=2, choices=visibility_choices)


class Board(models.Model):
    PRIVATE = 'PR'
    PUBLIC = 'PU'
    visibility_choices = {
        PRIVATE: 'Private',
        PUBLIC: 'Public'
    }
    name = models.CharField(max_length=255)
    description = models.TextField()
    visibility = models.CharField(max_length=2, choices=visibility_choices)
    