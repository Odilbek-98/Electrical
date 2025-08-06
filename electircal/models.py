from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    project = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name