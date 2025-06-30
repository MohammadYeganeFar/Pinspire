from django.shortcuts import render
from rest_framework import viewsets
from user_interactions.models import Like, Comment
from user_interactions.serializers import (LikeSerializer, 
                                           CommentSerializer)

class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()