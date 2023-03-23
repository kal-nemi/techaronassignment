from django.contrib import admin
from django.urls import path,include
from rest_framework import viewsets,routers
from .views import UserViewSet,UserProfileViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofile',UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]