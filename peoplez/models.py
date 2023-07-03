from django.db import models

# Create your models here.
"""
1. kameHouse % python3 manage.py makemigrations after creating new model
2. python3 manage.py migrate 
3. register model in index/admin file
"""


# about us section
class Introduction(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='peoplez/', blank=False)  # we have to pip install "pillow" to use upload_to

    def __str__(self):
        return self.title


class StoryTime(models.Model):
    description = models.TextField(max_length=2500, blank=False)
    image1 = models.ImageField(upload_to='peoplez/', blank=False)
    image2 = models.ImageField(upload_to='peoplez/', blank=False)
    image3 = models.ImageField(upload_to='peoplez/', blank=False)

    def __str__(self):
        return "dragon story"

