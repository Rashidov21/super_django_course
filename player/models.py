from django.db import models

# Create your models here.


class Players(models.Model):
    number = models.IntegerField(default=0, blank=True)
    player = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)
    dr = models.DateField(blank=True)
    height = models.PositiveIntegerField(default=0, blank=True)
    weight = models.PositiveIntegerField(default=0, blank=True)
    price = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.player)


# class TestModel(models.Model):
#     COUNTRIES = (
#         ("USA", 'usa'),
#         ("China", 'china'),
#     )
#     binf = models.BinaryField() # 0 1
#     boolf = models.BooleanField(default=False, null=True) # checkbox
#     # boolf = models.NullBooleanField(default=False) # checkbox
#     datef = models.DateField() # YYYY-MM-DD
#     timef = models.TimeField() # HH:MM:SS
#     datetimef = models.DateTimeField(auto_now_add=True) # joriy sana va vaqt
#     duraf = models.DurationField() # vaqt interval 
#     # autof = models.AutoField() # id 
#     bigif = models.BigIntegerField() # -922326546845641651 9212646456165541
#     decf = models.DecimalField(max_digits=6,decimal_places=4) # 22.4444
#     floatf = models.FloatField() # float 1.3
#     intf = models.IntegerField() # int 1
#     postintf = models.PositiveIntegerField() # 0 - 2147483647
#     postintf = models.PositiveBigIntegerField() # 0 - 32767
#     smalinf = models.SmallIntegerField() # -32767 - 32767
#     charf = models.CharField(max_length=100,
#                              verbose_name="Enter your name", 
#                              help_text="Only alphabet chars.",
#                              default="John Doe",
#                              null=True,
#                              blank=True,
#                              choices=COUNTRIES) # input
#     textf = models.TextField() # textarea
#     emailf = models.EmailField() #@gmail.com
#     filef = models.FileField() # file path str
#     filepathf = models.FilePathField() # file path max len 100
#     imgf = models.ImageField(upload_to='file path') # img
#     slugf = models.SlugField(max_length=100) # unique str
#     urlf = models.URLField() # url
#     uuidf = models.UUIDField() # 34sddihah24

#     class Meta:
#         verbose_name = "My test model"
#         verbose_name_plural = "MyTestModels"
#         ordering = ["title" ,"-published_date"]