from django.db import models

class Contractor(models.Model):
    TRADE_CHOICES = (
        ('electrician', 'Electrician'),
        ('plumber', 'Plumber'),
        ('carpenter', 'Carpenter'),
        ('painter', 'Painter'),
        ('mason', 'Mason'),
        ('general', 'General Contractor'),
    )

    name = models.CharField(max_length=200)
    trade = models.CharField(max_length=50, choices=TRADE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
