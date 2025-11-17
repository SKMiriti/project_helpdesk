from django.urls import path
from . import views

app_name = 'communication'

urlpatterns = [
    path('', views.home, name='home'),
    path('comments/', views.comments, name='comments'),
    path('notifications/', views.notifications, name='notifications'),
]
