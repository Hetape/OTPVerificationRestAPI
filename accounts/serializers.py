import imp
from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import Role

User = get_user_model()

# Create your serializers here.

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "fname", "lname", "phone" ,"email","address","city","state","country","image","image"]
        extra_kwargs = {
            "id": {"read_only": True},
            "fname": {"required": True},
            "lname": {"required": True},
            "phone": {"required": True},
            "email": {"required": True},
        }


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user