from django.db import models
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.alerts.exists():
            Alert.objects.create(product=self, days_before_expiration=5)
            Alert.objects.create(product=self, days_before_expiration=10)

    def __str__(self):
        return self.name

class Alert(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="alerts")
    days_before_expiration = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def check_alert_status(self):
        today = now().date()
        days_left = (self.product.expiration_date - today).days

        if days_left <= 0:
            return "Expirado"
        elif days_left < 5:
            return "Alerta: Menos de 5 días"
        elif days_left < 10:
            return "Alerta: Menos de 10 días"
        else:
            return "Vigente"

    def __str__(self):
        return f"Alerta para: {self.product.name} - {self.check_alert_status()}"