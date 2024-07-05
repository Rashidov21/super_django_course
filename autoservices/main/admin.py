from django.contrib import admin
from .models import Category,ServiceType,Service,Gallery,Rating
# Register your models here.

admin.site.register(Category)
admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(Gallery)
admin.site.register(Rating)