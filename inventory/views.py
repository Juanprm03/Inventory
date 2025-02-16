# Create your views here.
from rest_framework import viewsets
from .models import Product, Alert
from .serializers import ProductSerializer, AlertSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import timedelta
from django.utils.timezone import now

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Product.objects.all()
        status = self.request.query_params.get('status')

        if status == "expirado":
            return queryset.filter(expiration_date__lt=now().date())
        elif status == "alerta_5":
            return queryset.filter(expiration_date__range=[now().date(), now().date() + timedelta(days=5)])
        elif status == "alerta_10":
            return queryset.filter(expiration_date__range=[now().date(), now().date() + timedelta(days=10)])

        return queryset

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]
