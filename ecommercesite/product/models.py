from django.db import models
import uuid

# Create your models here.

'''
Product:
	productMainModel:
		Title:
		Description:
		Unique_id:unique
		Price:
		
	productImageModel:
		product:FK(productMainModel)
		image:IF



'''
class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(verbose_name="Description")
    price = models.IntegerField()
    # uid = models.UUIDField( default=uuid.uuid4(), editable=False)

def productpath(instance,filename):
    return 'images/{title}/{filename}'.format(title = instance.title,filename=filename)

class ProductImageModel(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product ", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=productpath)
