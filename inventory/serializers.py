from rest_framework import serializers
from .models import Product, Alert

class AlertSerializer(serializers.ModelSerializer):
    alert_status = serializers.SerializerMethodField()

    class Meta:
        model = Alert
        fields = '__all__'

    def get_alert_status(self, obj):
        return obj.check_alert_status()
    
class ProductSerializer(serializers.ModelSerializer):
    alerts = AlertSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
