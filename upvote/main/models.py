from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.title

class Reviews(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')    
    name = models.CharField(max_length=250)
    content = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Reviews'