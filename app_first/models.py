from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
