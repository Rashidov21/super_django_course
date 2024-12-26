from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    age = models.IntegerField(default=10)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Question(models.Model):
    question = models.CharField(max_length=350)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=350)
    question = models.ForeignKey(Question, on_delete=models.CASCADE )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


