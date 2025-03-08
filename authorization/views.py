from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest

def render_auth(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        
        print(f'Username: {username}\nPassword: {password}')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged successful!')
            return redirect('/')
        else:
            messages.error(request, 'Incorrect username or password. Try again')
            return redirect('auth')

    return render(request, 'authorization/auth.html')

def logout_user(request: HttpRequest):
    logout(request)
    messages.success(request, ( 'You were logged out!'))
    return redirect('/')
    
    