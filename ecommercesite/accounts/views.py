from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserCartSerializers,UserSerializer,UserProfileSerializer
from .models import User,UserProfile

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


    
