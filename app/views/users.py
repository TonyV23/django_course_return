from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from app.forms import UserForm

# Display users
def index(request):
    users = User.objects.all()
    return render(
        request,
        'app/users/index.html',
        {
            'users': users
        }
    )
    
# Show register form
def register(request):
    form = UserForm()
    return render(
        request, 
        'app/users/register.html',
        {
            'form': form
        }
    )

# Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password incorrect')
            
    return render(
        request,
        'app/users/login.html'
    )

# Register a new user    
def store(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
  
# Logout a user authenticated  
def user_logout(request):
    logout(request)
    return redirect('/login')