from django.shortcuts import render
from .models import Invoice
from django.contrib.auth.decorators import login_required

@login_required
def billing_dashboard(request):
    invoices = Invoice.objects.filter(user=request.user)
    return render(request, 'billing/billing_dashboard.html', {'invoices': invoices})

@login_required
def subscription_detail(request):
    return render(request, 'billing/subscription_detail.html')
