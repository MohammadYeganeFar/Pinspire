from rest_framework import serializers
from core.models import Pin, Board

class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    pins = PinSerializer(many=True, read_only=True)
    
    class Meta:
        model = Board
        fields = '__all__'
        

class AddPinToBoardSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    visibility = serializers.CharField(read_only=True)
    
    class Meta:
        model = Board
        fields = ['name',  'visibility', 'pins', 'description']