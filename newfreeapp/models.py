from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    Description = models.TextField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='course', null= True, blank= True)