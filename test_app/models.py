from django.db import models

# Create your models here.
class Parent(models.Model):
    name = models.CharField(max_length=50)

class Child(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    favorite_siblings = models.ManyToManyField("self", symmetrical=False, blank=True)

    def __str__(self):
        return self.name
    
