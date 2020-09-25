from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Kategoriya nomi', max_length=90)
    slug = models.SlugField('Slag', max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    title = models.CharField('Nomi', max_length=200)
    slug = models.SlugField('Slag', max_length=50, unique=True)
    category
    def __str__(self):
        pass

class OrderItem(models.Model):
    pass

    def __str__(self):
        pass

class Order(models.Model):
    pass

    def __str__(self):
        pass