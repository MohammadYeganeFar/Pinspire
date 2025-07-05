from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import P
from django_filters.rest_framework import (DjangoFilterBackend,
                                            )
from shop_manage.serializers import (ProductSerializer, 
                                    CategorySerializer, 
                                    OrderSerializer)
from shop_manage.models import Product, Category, Order
from shop_manage.filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = (Product.objects.all())
    filter_backends = [DjangoFilterBackend, 
                       SearchFilter, 
                       OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name','description','category__name']
    search_param = 'q'
    # ordering_fields = ['name', 'price', 'is_available', 'created_at']
    ordering_fields = '__all__'
    ordering = ['name']
    
    def list(self, request, *args, **kwargs):
        products = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()