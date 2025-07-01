from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, 
                                                    TokenRefreshView)
from account.views import CustomUserViewSet


router = DefaultRouter()
router.register(r'users', CustomUserViewSet, 'users')

urlpatterns = [
    path('auth/register/', CustomUserViewSet.as_view(
        {
            'post': 'create'
        }
    ), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('', include(router.urls))
]