from django.db import models

# Create your models here.
class User(models.Model):
    requirements = models.CharField(max_length=50)
    link = models.CharField(max_length=60)
    quantity = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    description = models.TextField()


    def __str__(self):
        return self.name