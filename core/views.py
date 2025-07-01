from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Pin, Board
from core.serializers import PinSerializer, BoardSerializer

class PinViewSet(viewsets.ModelViewSet):
    serializer_class = PinSerializer
    queryset = Pin.objects.all()
    
    def list(self, request):
        pins = Pin.objects.filter(visibility='PU')
        serializer = self.get_serializer(pins, many=True)
        return Response(serializer.data)
        


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    
    def list(self, request):
        boards = Board.objects.filter(visibility='PU')
        serializer = self.get_serializer(boards, many=True)
        return Response(serializer.data)
        