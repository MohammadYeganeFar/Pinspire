from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import (DjangoFilterBackend,
                                            )
from shop_manage.serializers import (ProductSerializer, 
                                    CategorySerializer, 
                                    OrderSerializer)
from shop_manage.models import Product, Category, Order
from shop_manage.filters import ProductFilter


class ProductPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 3
    page_size_query_param = 'page_size'


class CustomSearchFilter(SearchFilter):

    # Using 'q' instead of 'search'
    search_param = 'q'


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    queryset = (Product.objects.all())

    filter_backends = [DjangoFilterBackend, 
                       CustomSearchFilter, 
                       OrderingFilter]
    
    filterset_class = ProductFilter

    search_fields = ['name','description','category__name']

    # ordering_fields = ['name', 'price', 'is_available', 'created_at']
    ordering_fields = '__all__'
    
    ordering = ['name']

    pagination_class = ProductPagination
    

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()