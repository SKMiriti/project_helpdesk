from django.contrib import admin
from django.urls import path, include  # include is needed to reference app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('communication/', include('communication.urls')),  # routes to communication app
    path('billing/', include('billing.urls')),              # routes to billing app
]
