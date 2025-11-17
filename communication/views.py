from django.shortcuts import render
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'communication/home.html', {'messages': messages})

@login_required
def comments(request):
    return render(request, 'communication/comments.html')

@login_required
def notifications(request):
    return render(request, 'communication/notifications.html')
