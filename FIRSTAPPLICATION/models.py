from django.db import models

# Create your models here.

class Name(models.Model):
    #declaring the filed of the Name Model
    name = models.CharField(max_length=20)



    def __str__(self):
        return self.name

class Age(models.Model):
    #declaring the filed of the ID Model
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.age#attribute

class Address(models.Model):
    #declaring the field of the Address model
    address = models.CharField(max_length=12)
    def __str__(self):
        return self.address

class Email(models.Model):
    #declaring the field of the Address model
    email = models.EmailField(max_length = 200)


    def __str__(self):
        return self.email

