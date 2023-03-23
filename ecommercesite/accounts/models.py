from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from product.models import Product
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
'''
User Model:
	Phone_number:unique
	Email:EF
	is_customer:BF
	is_admin:BF
userProfileModel:
	owner:OTO(User)
	Name:
	Date_of_birth:
	Gender:choices(MALE,FEMALE,OTHERS)
	Image:

user login topModel:
	owner:FK(User)
	Otp:IF
	active:BF

UserCartProductModel:
	owner:FK(User)
	product:FK(productMainModel)
	status:Choices(pending,completed)

UserCartModel:
	owner:OTO(User)
	products:MTM(UserCartProductModel)
	price:


'''

class User(models.Model):
    phoneno = PhoneNumberField(unique = True)
    email = models.EmailField(max_length=254)
    is_customer = models.BooleanField()
    is_admin = models.BooleanField()


    def __str__(self):
        return self.email


class UserProfile(models.Model):
    owner = models.OneToOneField(User, verbose_name="owner info", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob =  models.DateField()
    genderChoices = (
        ('Male', 'Male'),
        ('Female','Female'),
        ('Others', 'Others')
    )
    gender = models.CharField(choices=genderChoices,max_length=10)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.owner

class UserLoginTopModel(models.Model):
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)
    OTP  = models.IntegerField()
    active = models.BooleanField()

class UserCartProduct(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    statuschoices = (
        ('Pending','Pending'),
        ('Completed','Completed')
    )
    status = models.CharField(choices=statuschoices,max_length=20)

class UserCart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(UserCartProduct)
    price = models.IntegerField()






