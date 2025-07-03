from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from core.models import Pin, Board
from core.serializers import (PinSerializer, 
                                                BoardSerializer, 
                                                AddPinToBoardSerializer)
from account.models import CustomUser
from rest_framework.permissions import IsAuthenticated

class PinViewSet(viewsets.ModelViewSet):
    serializer_class = PinSerializer
    queryset = Pin.objects.all()
    permission_classes = [IsAuthenticated]
    
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
    
    def create(self, request):
        # checking uniquness of user boards names
        #user = request.user 
        user = CustomUser.objects.get(username='user20')# just for test
        board_name = request.data.get('name')
        print('\n1hiii')
        if Board.objects.filter(name=board_name, owner=user).exists():
            print('\n2hiii')
            return Response({'error': f'Board with name {board_name} already exist. USE THAT!'})
        print('\n3hiii')
        return super().create(self, request)
    
    def wishlist(self, request):
        #user = request.user 
        user = CustomUser.objects.get(username='user20')# just for test
        try:
            user_wishlist = Board.objects.get(name='wishlist', owner=user)
            # user_wishlist = Board.objects.get_user_wishlist(user=user)
        except Board.DoesNotExist:
            return Response({'message': 'You dont have a wishlist.'})
        pins = user_wishlist.pins.all()
        serializer = PinSerializer(pins, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def add_pin_to_board(request, pk):
    board = Board.objects.get(pk=pk)
    serializer = AddPinToBoardSerializer(board)
    
    if request.method == 'GET':
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AddPinToBoardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pin_id = request.data.get('pins')
        pin = Pin.objects.get(id=pin_id)
        board.pins.add(pin)
        serializer = BoardSerializer(board)
        return Response(serializer.data, status.HTTP_201_CREATED)
        

#@api_view(['POST', 'DELETE'])
#def edit_wishlist(request, pin_id):
    