from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.http import HttpRequest

def render_registration(request: HttpRequest):
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create(username= username, email= email)
            user.set_password(password)
            user.save()

            messages.success(request, 'You were successfully registered!')
            return redirect('auth')
    
    return render(request, 'registration/reg.html', context= {'form': form})
