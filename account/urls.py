from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import CustomUserViewSet


router = DefaultRouter()
router.register(r'users', CustomUserViewSet, 'users')

urlpatterns = [
    path('', include(router.urls))
]