from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role=role)
        return redirect('login')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    role = request.user.profile.role
    return render(request, 'accounts/dashboard.html', {'role': role})

def logout_view(request):
    logout(request)
    return redirect('login')
