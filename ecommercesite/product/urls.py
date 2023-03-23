from django.contrib import admin
from django.urls import path,include
from rest_framework import viewsets,routers
from .views import ProductViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]