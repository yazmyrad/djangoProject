from django.shortcuts import render, redirect
from .forms import Registration, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, Http404
from .models import Profile
from django.contrib.auth.models import User

def profile_view(request, username):
    userid = User.objects.get(username=username)
    profile = Profile.objects.get(user = userid)
    return render(request, "profile/profile.html", {'profile':profile})

def register_view(request):
    if request.method == "POST":
        form = Registration(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect("/login")
    else:
        form = Registration()

    return render(request, "register/login.html", {"form":form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("/home")
    else:
        form = LoginForm()
    return render(request, "register/register.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect("/")