from django.db import models

class Fitness(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    instructor = models.CharField(max_length=100)
    available_slots = models.IntegerField(default=0)

    def __str__(self):
        return self.name
class Booking(models.Model):
    id  =  models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(unique=True)

    def __str__(self):
        return self.client_name
    
    