from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import ProductViewSet, AlertViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'alerts', AlertViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
