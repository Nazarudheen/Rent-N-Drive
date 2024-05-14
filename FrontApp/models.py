from django.db import models

# Create your models here.
class ReviewDB(models.Model):
    Name = models.CharField(max_length=100, null=True,blank=True)
    Email = models.CharField(max_length=100, null=True,blank=True)
    Image = models.ImageField(upload_to="Feedback_Image", null=True, blank=True)
    Review = models.CharField(max_length=200, null=True, blank=True)

class BookDB(models.Model):
    Name = models.CharField(max_length=100, null=True,blank=True)
    Email = models.CharField(max_length=100, null=True,blank=True)
    Car = models.CharField(max_length=100, null=True, blank=True)
    Number = models.IntegerField( null=True,blank=True)
    PickUpL = models.CharField(max_length=200, null=True, blank=True)
    DropOffL = models.CharField(max_length=100, null=True, blank=True)
    PickUp = models.CharField(max_length=100, null=True, blank=True)
    DropOff = models.CharField(max_length=100, null=True, blank=True)
    PickUpT =models.CharField(max_length=100, null=True, blank=True)

class SignUpDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
class DriverJobDB(models.Model):
    Name = models.CharField(max_length=100, null=True,blank=True)
    Email = models.CharField(max_length=100, null=True,blank=True)
    Number = models.IntegerField( null=True,blank=True)
    Experience = models.CharField(max_length=200, null=True, blank=True)
    Resume = models.FileField(upload_to="Resume_Driver")
