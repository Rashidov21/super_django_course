from django.db import models
from users.models import CustomUser

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="category/images/", blank=True)
    
    def __str__(self):
        return self.name
    

class ServiceType(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="services")
    
    def __str__(self):
        return self.name


DAYS_OF_WEEK = [
    ('mon', 'Dushanba'),
    ('tue', 'Seshanba'),
    ('wed', 'Chorshanba'),
    ('thu', 'Payshanba'),
    ('fri', 'Juma'),
    ('sat', 'Shanba'),
    ('sun', 'Yakshanba'),
]

PAYMENT_CHOICES = [
    ('pc', 'Plastik karta'),
    ('ca', 'Naqd pul'),
    ('bt', 'Bank oʻtkazmasi'),
]
class Service(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="service")
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="user_service")
    service_types = models.ManyToManyField(ServiceType)
    phone_1 = models.CharField(max_length=150, blank=True)
    phone_2 = models.CharField(max_length=150, blank=True)
    address_1 = models.CharField(max_length=150, blank=True)
    address_2 = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to="service/images/", blank=True)
    work_time_start = models.TimeField(blank=True,null=True)
    work_time_end = models.TimeField(blank=True,null=True)
    working_days = models.CharField(max_length=20, choices=DAYS_OF_WEEK, blank=True)
    description = models.TextField(blank=True)
    reyting_value = models.IntegerField(default=0)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, blank=True)
    
    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="service/images/", blank=True)
    
    def __str__(self):
        return self.service.title

class Rating(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="ratings")
    value = models.IntegerField(default=0)
    name = models.CharField(max_length=150, blank=True)
    comment = models.CharField(max_length=350,blank=True)
    
    def __str__(self):
        return self.value