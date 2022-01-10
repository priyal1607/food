from django.db import models
from django.db.models.deletion import CASCADE
class foodname(models.Model):
    names=models.CharField(max_length=20)
    def __str__(self):
        return self.names
class foods(models.Model):
    name=models.ForeignKey(foodname, on_delete=CASCADE)
    des=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='photo')
    img=models.ImageField(upload_to='photo')
    img=models.ImageField(upload_to='photo')
    desc=models.CharField(max_length=1000)
    


# Create your models here.
