from rest_framework import serializers
from accounts.models import User,UserCart,UserCartProduct,UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UserCartSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserCart
        fields = "__all__"

