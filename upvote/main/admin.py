from django.contrib import admin
from .models import Category,Comments,Post,Reviews
# Register your models here.


admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Post)
admin.site.register(Reviews)