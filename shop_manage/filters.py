from django_filters import rest_framework as filter
from shop_manage.models import Product


class ProductFilter(filter.FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'is_available': ['exact'],
            'price': ['gte', 'lte']
        }


