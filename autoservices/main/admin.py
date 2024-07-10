from django.contrib import admin
from .models import Category,ServiceType,Service,Gallery,Rating
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]

admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(Gallery)
admin.site.register(Rating)