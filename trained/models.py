from django.db import models

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Menuss(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    answer = models.CharField(max_length=50, unique=True,null= True,blank= True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

class Node(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,)
    answer = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name

# class ActivityLog(models.Model):
#     activity = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     ip_address = models.GenericIPAddressField()
#     device = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.activity

class Admin_panel(models.Model):
    heading = models.CharField(max_length=15,null=True,blank=True)
    image =  models.ImageField(upload_to='uploads/',blank=True)
    def __str__(self):
        return self.heading

class user_panel(models.Model):
    input_label = models.CharField(max_length=60,null=True,blank=True)
    input_type = models.CharField(max_length=78, null = True, blank = True)
    parent_id = models.IntegerField(default=0, blank=True, null=True)
    def __str__(self):
        return self.input_label

from django.db import models

class MyModel(models.Model):
    char_field = models.CharField(max_length=100)
    text_field = models.TextField()
    boolean_field = models.BooleanField()
    integer_field = models.IntegerField()
    float_field = models.FloatField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)
    date_field = models.DateField()
    datetime_field = models.DateTimeField()
    email_field = models.EmailField()
    url_field = models.URLField()
    file_field = models.FileField(upload_to='uploads/')
    image_field = models.ImageField(upload_to='images/')
    class Meta:
        managed = False
        db_table = 'my_table_name'

