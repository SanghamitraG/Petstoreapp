from django.db import models

# Create your models here.
class petstoreapp_db(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    details = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  
    image = models.ImageField(upload_to= 'images')
    
    def __str__(self):
        return self.name
