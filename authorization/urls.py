from .views import *
from django.urls import path


urlpatterns = [
    path('', render_auth, name= 'auth'),
]
