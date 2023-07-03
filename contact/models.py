from django.db import models


# Create your models here.
# contact us section
class ContactList(models.Model):
    address = models.TextField(max_length=800, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.email


class ContactForm(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=400, blank=False)
    message = models.TextField(max_length=800, blank=False)

    def __str__(self):
        return f"{self.subject} || From {self.name}"
