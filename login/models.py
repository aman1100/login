from django.db import models

# Create your models here.
class Signup(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    password = models.CharField(max_length=50,default="")
    designation = models.CharField(max_length=50,default="")
    gender = models.CharField(max_length=50,default="")
    address = models.CharField(max_length=500,default="")

