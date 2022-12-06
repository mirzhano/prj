from django.db import models
from django.db import models
# Create your models here.


class TvParser(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='')
	title_text = models.CharField(max_length=100, null=True)

def __str__(self):
	return self.title