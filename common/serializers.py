from rest_framework import serializers
from .models import *

# create serializer from here.
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id','name',]
    
    def create(self, validated_data):
        return State.objects.create(**validated_data)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','name','state']


    def create(self, validated_data):
        return City.objects.create(**validated_data)



class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id','name','category','city']


    def create(self, validated_data):
        return Area.objects.create(**validated_data)

