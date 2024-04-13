from django.db import models
class Register(models.Model):
    username=models.CharField(max_length=100)
    emailid= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    mobile= models.CharField(max_length=200)
    fullname= models.CharField(max_length=200)
    def __str__(self):
        return self.username + " " + self.emailid 