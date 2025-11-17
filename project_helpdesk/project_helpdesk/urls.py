from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('tickets/', include('tickets.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('communication/', include('communication.urls')),
    path('billing/', include('billing.urls')),
]
