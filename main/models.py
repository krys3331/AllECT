from distutils.command.upload import upload
from os import name
from platform import architecture
from pydoc import describe
from django.db import models

# Create your models here.

class ECT(models.Model):
    name = models.CharField(max_length = 256)
    describe = models.TextField(blank = True)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    amountRam = models.IntegerChoices
    processor = models.ForeignKey('Proccessor', on_delete=models.PROTECT, null=True, )
    cathegory = models.ForeignKey('Cathegory', on_delete=models.PROTECT, null=True, )
    
    def __str__(self) -> str:
        return self.name

class Proccessor(models.Model):
    name = models.CharField(max_length=128)
    describe = models.TextField(blank=True)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    architect = models.ForeignKey('Architecture', on_delete=models.PROTECT, null=True, )
    
    def __str__(self) -> str:
        return self.name
    
class Architecture(models.Model):
    name = models.CharField(max_length=16)
    describe = models.TextField(blank = True)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    
    def __str__(self) -> str:
        return self.name
    
class Cathegory(models.Model):
    name = models.CharField(max_length=128)
    describe = models.TextField(blank=True)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    
    def __str__(self) -> str:
        return self.name