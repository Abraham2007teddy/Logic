import uuid
from django.db import models

class CargoRequest(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_surname = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()
    from_country = models.CharField(max_length=100)
    to_country = models.CharField(max_length=100)
    cargo_type = models.CharField(max_length=100)
    description = models.TextField()
    agree_privacy_policy = models.BooleanField(default=False)
    agree_promotions = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name