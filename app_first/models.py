from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=16)
    price = models.FloatField(max_length=8)
    publish_date = models.DateField()
    press = models.CharField(max_length=16)


