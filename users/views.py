from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


def home(request):
    return render(request, 'users/home.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You successfully logged in. Hello ...")
            return redirect('home')
        else:
            messages.warning(request, "Wrong username / password. try again")
            return redirect('login')
    else:
        return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out! Bye...")
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, "You have successfully registered.")
            return redirect('login')
        else:
            messages.warning(request, "Something wrong. Please try again.")
            return redirect('register')
    else:
        return render(request, 'users/register.html', {'form':form})