import datetime
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
    
    class Meta:
        ordering = ["-id"]
    
    def get_published_days(self):
        _now = datetime.datetime.now()
        print( self.created_at.date())
        days = _now.date() - self.created_at.date()
        if days.days > 365:
            return days
        if days.days == 0:
            return "Posted today !"
        elif days.days == 1:
            return "Posted yesterday !"
        else:
            return f"Posted {days.days} days ago"
        

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
        
class Comments(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    comment = models.CharField(max_length=500)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
    
    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.name