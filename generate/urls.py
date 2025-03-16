from .views import *
from django.urls import path

urlpatterns = [
    path('', generate_qr, name= 'generate'),
]