from django.urls import path
from . import views

urlpatterns = [
    path('webhook/', views.webhook, name='webhook'), # This route will handle the webhook from Flutterwave.  
]
