from rest_framework import serializers
from accounts.models import User
from .models import *

# create serializer from here.
class TrackUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "fname", "lname", "phone" ,"email"]  # include whatever user fields you want to display
        extra_kwargs = {
            "id": {"read_only": True},
            "fname": {"required": True},
            "lname": {"required": True},
            "phone": {"required": True},
            "email": {"required": True},
        }

class TrackSerializer(serializers.ModelSerializer):
    trackuser = TrackUserSerializer()
    class Meta:
        model = Track
        fields = ['imgname','state','created_at','trackuser']