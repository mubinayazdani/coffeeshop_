from django.db import models

# Create your models here.

class Coffee(models.Model):
    
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='coffeee/pimg')
    
    def __str__(self):
        
        return f'{self.name}'




class Reservation(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(null=True)
    time = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.name}'

class contactt_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
