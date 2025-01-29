from .views import *
from django.urls import path


urlpatterns = [
    path('', render_plan_settings, name= 'plan_settings'),
]