from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    subscribers = models.ManyToManyField(User)

class CreditCard(models.Model):
    number = models.IntegerField()
    expiry = models.DateField('Expiration Date')
    cvv = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)