from django.contrib import admin
from .models import Answer ,Category, Question
# Register your models here.

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id','answer', 'question', 'category')
    list_editable = ('question', 'category')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question')
    list_editable = ('question',)
    list_filter = ('question',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    # list_editable = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    
