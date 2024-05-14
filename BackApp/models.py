from django.db import models

# Create your models here.
class CarDB(models.Model):
    ModelName = models.CharField(max_length=100, null=True,blank=True)
    Brand = models.CharField(max_length=100, null=True,blank=True)
    Transmission = models.CharField(max_length=100, null=True,blank=True)
    Discription = models.CharField(max_length=100, null=True,blank=True)
    Fuel = models.CharField(max_length=100, null=True,blank=True)
    Price = models.IntegerField( null=True,blank=True)
    PriceD = models.IntegerField(null=True,blank=True)
    PriceDD = models.IntegerField(null=True,blank=True)
    Mileage = models.IntegerField(null=True,blank=True)
    Seats = models.IntegerField(null=True,blank=True)
    Luggage = models.IntegerField(null=True,blank=True)
    Image = models.ImageField(upload_to="Car_Image", null=True, blank=True)

class DriverDB(models.Model):
    Name = models.CharField(max_length=100, null=True,blank=True)
    Language = models.CharField(max_length=100, null=True,blank=True)
    Experience = models.CharField(max_length=100, null=True,blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Number = models.IntegerField(null=True, blank=True)
    Rating = models.CharField(max_length=100,null=True, blank=True)
    Image = models.ImageField(upload_to="Driver_Image", null=True, blank=True)

class BlogDB(models.Model):
    Head = models.CharField(max_length=100, null=True,blank=True)
    SDiscription = models.CharField(max_length=100, null=True,blank=True)
    Discription = models.CharField(max_length=100, null=True,blank=True)
    Image = models.ImageField(upload_to="Blog_Image", null=True, blank=True)
