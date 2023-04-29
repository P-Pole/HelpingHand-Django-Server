from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from charities.models import Charities
from charities.models import User
from .serializers import CharitiesSerializer, UserSerializer
# Create your views here.

class CharitiesViewSet(viewsets.ViewSet):

    def list(self, request): #/api/charities  GET
        charities = Charities.objects.all()
        serializer = CharitiesSerializer(charities, many=True)

        return Response(serializer.data) #if serializer.data else Response([])
    
    def create(self, request): # POST
        serializer = CharitiesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request,pk=None): #/api/products/<str:id>
        charity = Charities.objects.get(id=pk)
        serializer = CharitiesSerializer(charity)

        return Response(serializer.data)
    
    def update(self, request, pk=None): #same as retrieve
        charity = Charities.objects.get(id=pk)
        serializer = CharitiesSerializer(instance=charity, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #same as retrieve
        charity = Charities.objects.get(id=pk)
        charity.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserViewSet(viewsets.ViewSet):
    
    def list(self, request): #/api/users  GET
        charities = User.objects.all()
        serializer = UserSerializer(charities, many=True)

        return Response(serializer.data) #if serializer.data else Response([])

    def create(self, request): # POST
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request,pk=None): #/api/users/<str:id>
        charity = User.objects.get(id=pk)
        serializer = UserSerializer(charity)

        return Response(serializer.data)
    
    def update(self, request, pk=None): #same as retrieve
        charity = User.objects.get(id=pk)
        serializer = UserSerializer(instance=charity, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #same as retrieve
        charity = User.objects.get(id=pk)
        charity.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    