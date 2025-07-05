from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, 
                                on_delete=models.CASCADE,
                                related_name='products',
                                )
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    customer_name = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField(Product, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    