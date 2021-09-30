from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField(max_length=400)
    financing = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}"
# Create your models here.
