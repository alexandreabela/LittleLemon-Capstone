from django.db import models

# Create your models here.
class Booking(models.Model): 
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateField()

class MenuItem(models.Model): 
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
