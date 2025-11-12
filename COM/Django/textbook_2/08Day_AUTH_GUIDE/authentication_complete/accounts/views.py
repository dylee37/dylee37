from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')

from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')


from .forms import CustomUserChangeForm
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, isinstance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)