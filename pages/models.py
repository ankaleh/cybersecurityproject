from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    

class Message(models.Model):
    text = models.CharField(max_length=200)
    sent_from = models.ForeignKey(Person, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

class Cottage(models.Model):
    name = models.TextField()
    rooms = models.IntegerField()
    rent = models.IntegerField()

class Reservation(models.Model):
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    #paid = models.BooleanField(default=False)



