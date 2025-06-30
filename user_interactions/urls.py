from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_interactions.views import LikeViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'likes', LikeViewSet, 'like')
router.register(r'comments', CommentViewSet, 'comment')

urlpatterns = [
    path('', include(router.urls))
]