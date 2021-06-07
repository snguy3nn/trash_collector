from django.db import models

# Create your models here.
<<<<<<< HEAD
=======
class Employee(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=50)
# TODO: Create an Employee model with properties required by the user stories
>>>>>>> 6b835f58ed6e9d9583e0164e5925cc9d9a2aebaa


class Employee(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=50)
