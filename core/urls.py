from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import PinViewSet, BoardViewSet, add_pin_to_board


router = DefaultRouter()
router.register(r'pins', PinViewSet, 'pin')
router.register(r'boards', BoardViewSet, 'board')

urlpatterns = [
    path('boards/<int:pk>/pins/', add_pin_to_board),
    path('', include(router.urls)),
]