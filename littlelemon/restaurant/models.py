from django.db import models

# Create your models here.

class Booking(models.Model):
    #id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.IntegerField(default=1)  
    booking_date = models.DateTimeField()

class Menu(models.Model):
    #id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
