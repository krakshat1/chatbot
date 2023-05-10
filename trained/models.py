from django.db import models

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Menuss(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    answer = models.CharField(max_length=50, unique=True,null= True,blank= True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']