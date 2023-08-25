from django.db import models

# Create your models here.

class book(models.Model):
    name = models.CharField(max_length=30)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default="guest")
    email = models.EmailField(blank=True)
    description = models.TextField(default="available in our library")

    def __str__(self):
        return self.name
    
