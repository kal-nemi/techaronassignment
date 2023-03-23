from django.contrib import admin
from .models import User,UserCart,UserCartProduct,UserProfile

# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    # fields = "__all__"
    pass

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


