from django.db import models

# Create your models here.
"""
1. kameHouse % python3 manage.py makemigrations after creating new model
2. python3 manage.py migrate 
3. register model in index/admin file
"""


# about us section
class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)  # we have to pip install "pillow" to use upload_to

    def __str__(self):
        return self.title


# image slider on home page
class Slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)  # created new folder in Media called slider

    def __str__(self):
        return self.title

#class Insta_cap()
