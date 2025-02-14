from django.db import models

class Contact(models.Model):
    username = models.CharField(max_length=100, unique=True)
    phone_1 = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20, blank=True, null=True)  # Optional field

    def __str__(self):
        return self.username
