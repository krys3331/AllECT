from django.db import models
from django.urls import reverse
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
    
    def get_absolute_url(self):
        return reverse("ect", kwargs={"slug": self.slug})
    

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