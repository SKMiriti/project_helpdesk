from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('', views.billing_dashboard, name='billing_dashboard'),
    path('subscription/', views.subscription_detail, name='subscription_detail'),
]
