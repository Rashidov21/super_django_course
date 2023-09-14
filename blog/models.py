from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

from django_quill.fields import QuillField

# Create your models here.
class Category(models.Model):
    title = models.CharField('Category name *',max_length=50)
    icon = models.CharField('Font Awesome icon name *',max_length=50,blank=True)
    slug = models.SlugField('*',max_length=25, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    # def get_url(self):
    #     return reverse("blog:category_list", kwargs={"category_slug":self.slug})

    def __str__(self):
        return "{}".format(self.title)

class Tag(models.Model):
    title = models.CharField('Tag name *',max_length=50)
    icon = models.CharField('Font Awesome icon name *',max_length=50,blank=True)
    slug = models.SlugField('*',max_length=25, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        
    # def get_url(self):
    #     return reverse("main:tag_list", kwargs={"tag_slug":self.slug})

    def __str__(self):
        return "{}".format(self.title)


class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField("*",max_length=200, unique=True)
    body = QuillField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='posters/%Y-%m-%d')
    icon = models.CharField('Font Awesome icon name *',max_length=50, blank=True, null=True)
    up = models.PositiveIntegerField(default=0)
    down = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, related_name='categories')
    tag = models.ManyToManyField(Tag, related_name='tags')
    published = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Posts"
        ordering = ["-id"]
        
    def __str__(self):
        return self.title


    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments', null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.name