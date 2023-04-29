from rest_framework import serializers
from .models import Charities, User


class CharitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charities
        fields= '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'