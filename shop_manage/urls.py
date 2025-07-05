from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop_manage.views import ProductViewSet, CategoryViewSet


router = DefaultRouter()
router.register('products', ProductViewSet, 'product')
router.register('category', CategoryViewSet, 'category')

urlpatterns = [
    path('', include(router.urls))
]


