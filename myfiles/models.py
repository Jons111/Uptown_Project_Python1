from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Service(models.Model):
    nomi = models.CharField(max_length=50)
    manzil = models.CharField(max_length=100)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    rooms = models.IntegerField()
    bath_rooms= models.IntegerField()
    maydon = models.FloatField()
    rasm = models.ImageField(upload_to='media')
    vaqt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)