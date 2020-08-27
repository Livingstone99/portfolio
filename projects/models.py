from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to= 'images/')
    framework = models.CharField(max_length=100, default= 'python development')
    summary  = models.CharField(max_length = 200
                                )

