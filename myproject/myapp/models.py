from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    parent = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name

class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.flavor

class IceCreamKiosk(models.Model):
    location = models.CharField(max_length=100)
    ice_creams = models.ManyToManyField(IceCream, related_name='kiosks')

    def __str__(self):
        return self.location
