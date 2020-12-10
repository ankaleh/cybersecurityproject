from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    ssn = models.TextField(default="")
    

class Message(models.Model):
    content = models.TextField()
    sender = models.TextField(default="")

class Cottage(models.Model):
    name = models.TextField()
    rooms = models.IntegerField()
    rent = models.IntegerField()

class Reservation(models.Model):
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    count = models.IntegerField(default=0)
    #paid = models.BooleanField(default=False)
