from distutils.command.upload import upload
from os import name
from platform import architecture
from pydoc import describe
from django.db import models

# Create your models here.

class ECT(models.Model):
    slug = models.SlugField(unique=True, max_length=64, db_index=True, verbose_name="URL")
    name = models.CharField(max_length = 256)
    describe = models.TextField(blank = True)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    amountRam = models.IntegerChoices
    processor = models.ForeignKey('Proccessor', on_delete=models.PROTECT )
    cathegory = models.ForeignKey('Cathegory', on_delete=models.PROTECT )
    
    def __str__(self) -> str:
        return self.name

class Proccessor(models.Model):
    slug = models.SlugField(unique=True, max_length=64, db_index=True, verbose_name="URL")
    name = models.CharField(max_length=128)
    describe = models.TextField(blank=True)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    architect = models.ForeignKey('Architecture', on_delete=models.PROTECT )
    
    def __str__(self) -> str:
        return self.name
    
class Architecture(models.Model):
    slug = models.SlugField(unique=True, max_length=64, db_index=True, verbose_name="URL")
    name = models.CharField(max_length=16)
    describe = models.TextField(blank = True)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    
    def __str__(self) -> str:
        return self.name
    
class Cathegory(models.Model):
    slug = models.SlugField(unique=True, max_length=64, db_index=True, verbose_name="URL")
    name = models.CharField(max_length=128)
    describe = models.TextField(blank=True)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    
    def __str__(self) -> str:
        return self.name