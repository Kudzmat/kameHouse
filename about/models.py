from django.db import models

# Create your models here.
"""
1. kameHouse % python3 manage.py makemigrations after creating new model
2. python3 manage.py migrate 
3. register model in index/admin file
"""


# about us section
class Team(models.Model):
    name = models.CharField(max_length=100, blank=False)
    position = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='team/', blank=False)  # we have to pip install "pillow" to use upload_to

    def __str__(self):
        return f"{self.name} || {self.position}"
