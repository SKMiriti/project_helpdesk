from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Update with your login URL name
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})
