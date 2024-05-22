from django.contrib import admin
from .models import *
# Register your models here.





@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    prepopulated_fields = {"slug":("name",)}
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    prepopulated_fields = {"slug":("name",)}
    
    
@admin.register(Genre)
class GanreAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    prepopulated_fields = {"slug":("name",)}
    
    
    
admin.site.register(Comment)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id","title")
    prepopulated_fields = {"slug":("title",)}
    
admin.site.register(Role)