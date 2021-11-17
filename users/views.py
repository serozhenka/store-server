from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User

def login(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context = {
            'form': form,
        }

        return render(request, 'users/login.html', context)
    else:
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

        return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == "GET":
        form = UserRegistrationForm()

        context = {
            'form': form,
        }
        return render(request, 'users/register.html', context)
    else:
        form = UserRegistrationForm(data=request.POST)

        context = {
            'form': form,
            'error': None,
        }

        if User.objects.filter(username=request.POST['username']):
            context['error'] = 'Username has already been taken'
            return render(request, 'users/register.html', context)

        if request.POST['password1'] != request.POST['password2']:
            context['error'] = 'Passwords didn\'t match'
            return render(request, 'users/register.html', context)

        if form.is_valid():
            form.save()
            messages.success(request, 'Authorized successfully')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            context['error'] = 'Make sure your password satisfy certain conditions'
            return render(request, 'users/register.html', context)


def profile(request):
    if request.method == "GET":
        form = UserProfileForm(instance=request.user)
        context = {
            'form': form,
        }

        return render(request, 'users/profile.html', context)
    else:
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))