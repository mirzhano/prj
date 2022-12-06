from django.db import models

# Create your models here.
class Series(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    cost = models.IntegerField()
    characteristic = models.TextField(null=True)
