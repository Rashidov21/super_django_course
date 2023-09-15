from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','icon')
    list_display_links = ['title']
    list_filter = ['id']
    # list_editable = ['title']
    
    prepopulated_fields = {"slug":('title',)}
    
    def get_obj_icon(self, obj):
        return mark_safe(f'<i class="{obj.icon}"><i/>')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','title','icon')
    list_display_links = ['title']
    list_filter = ['id']
    # list_editable = ['title']
    
    prepopulated_fields = {"slug":('title',)}
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','views')
    list_display_links = ['title']
    list_filter = ['author','views', 'category']
    list_per_page = 10
    # list_editable = ['title']
    
    prepopulated_fields = {"slug":('title',)}
    
    # def get_obj_image(self, obj):
        # return mark_safe(f'<img src="{obj.image.url}" width="50" />')