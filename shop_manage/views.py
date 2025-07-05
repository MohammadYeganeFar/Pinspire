from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from shop_manage.serializers import (ProductSerializer, 
                                    CategorySerializer, 
                                    OrderSerializer)
from shop_manage.models import Product, Category, Order
from shop_manage.filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = (Product.objects.all())
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    
    def list(self, request, *args, **kwargs):
        products = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()