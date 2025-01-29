from .views import *
from django.urls import path


urlpatterns = [
    path('', render_my_QrCode, name= 'my_qrcode'),
]