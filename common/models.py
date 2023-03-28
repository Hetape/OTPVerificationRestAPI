from django.utils.text import slugify 
from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_del = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(State,self).save(*args,**kwargs)

    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_del = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE ,default=1)

    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(City,self).save(*args,**kwargs)

    def __str__(self):
        return self.name



class Area(models.Model):
    CATEGORY_CHOICES = (("Taluk", "Taluk"),("Village", "Village"),("District", "District"))
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_del = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="Village")
    city = models.ForeignKey(City, on_delete=models.CASCADE,default=1)


    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Area,self).save(*args,**kwargs)

    def __str__(self):
        return self.name