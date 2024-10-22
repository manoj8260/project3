from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomerProfile(models.Model):
     username=models.ForeignKey(User,on_delete=models.CASCADE)
     pno=models.CharField(max_length=50)
     profile_pic=models.ImageField(upload_to='customerprofile_pics/')

     def __str__(self):
          return self.username.username