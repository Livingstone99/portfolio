from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to= 'images/')
    framework = models.CharField(max_length=100, default= 'python development')
    summary  = models.CharField(max_length = 200
                                )
class FeedBack(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    feedback = models.TextField(max_length=500)
    def __str__(self):
        return self.name
