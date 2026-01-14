from django.urls import path
from .views import index, buy_car

urlpatterns = [
    path('', index, name='index'),
    path('buy/', buy_car, name='buy'),
]