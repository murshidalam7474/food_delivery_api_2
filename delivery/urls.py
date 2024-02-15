# delivery/urls.py

from django.urls import path
from .views import calculate_delivery_price

urlpatterns = [
    path('calculate_price/', calculate_delivery_price, name='calculate_delivery_price'),
]
