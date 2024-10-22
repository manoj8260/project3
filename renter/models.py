from django.db import models

# Create your models here.
class Brand(models.Model):
    company=models.CharField(max_length=50,primary_key=True)


    def __str__(self) :
        return self.company
    
class Bike(models.Model):
    company=models.ForeignKey(Brand,on_delete=models.CASCADE)
    bike_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='bike_photos')

    def __str__(self) -> str:
        return self.bike_name
