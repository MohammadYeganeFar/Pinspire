from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import PinViewSet, BoardViewSet


router = DefaultRouter()
router.register(r'pins', PinViewSet, 'pin')
router.register(r'boards', BoardViewSet, 'board')

urlpatterns = [
    path('', include(router.urls))
]