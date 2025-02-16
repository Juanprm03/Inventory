from celery import shared_task
from django.utils.timezone import now
from .models import Product

@shared_task
def check_product_alerts():
    today = now().date()
    for product in Product.objects.all():
        days_left = (product.expiration_date - today).days
        if days_left == 10 or days_left == 5:
            print(f"🔔 Alerta: {product.name} está por caducar en {days_left} días")
        elif days_left == 0:
            print(f"🚨 {product.name} ha caducado")