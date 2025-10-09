from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6)
    bookingDate = models.DateTimeField()

    class Meta:
        ordering = ['-bookingDate'] #show newest bookings first by default
    
    def __str__(self):
        return f"{self.name} for {self.no_of_guests} on {self.bookingDate.strftime('%Y-%m-%d')} at {self.bookingDate.strftime('%H:%M')}"

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : £{str(self.price)} : {str(self.inventory)}' #provides a human readable title instead of object.