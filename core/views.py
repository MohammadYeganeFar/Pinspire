from django.shortcuts import render
from rest_framework import viewsets
from core.models import Pin, Board
from core.serializers import PinSerializer, BoardSerializer

class PinViewSet(viewsets.ModelViewSet):
    serializer_class = PinSerializer
    queryset = Pin.objects.all()


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()