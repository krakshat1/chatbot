from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    question1 = models.CharField(max_length=30,null = True)
    answer1 = models.CharField(max_length=100,null  = True,blank = True)
    
    def __str__(self):
        return self.question1
class Submenu(models.Model):
    name = models.CharField(max_length=50,null = True)
    menu = models.ManyToManyField(Menu, null=True, related_name='submenues')
    answer1 = models.CharField(max_length=60,null = True, blank=True)
    
    def __str__(self):
        return self.name