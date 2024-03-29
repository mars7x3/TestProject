from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)


class Color(models.Model):
    title = models.CharField(max_length=50)


class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    colors = models.ManyToManyField(Color, related_name='products')


class ProductData(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='data')
    vendor_code = models.CharField(max_length=30)
    made_in = models.CharField(max_length=30)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products-images')

