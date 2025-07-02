from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from core.models import Pin, Board
from core.serializers import (PinSerializer, 
                                                BoardSerializer, 
                                                AddPinToBoardSerializer)

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

@api_view(['GET', 'POST'])
def add_pin_to_board(request, pk):
    board = Board.objects.get(pk=pk)
    serializer = AddPinToBoardSerializer(board)
    
    if request.method == 'GET':
        return Response(serializer.data)
    
    elif request.method == 'POST':
        print('request.data', request.data)
        serializer = AddPinToBoardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        print(obj)
        return Response(serializer.data, status.HTTP_201_CREATED)