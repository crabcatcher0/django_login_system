from django.shortcuts import render, redirect
from .forms import *

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def homepage(request):

    return render(request, 'signup/index.html')


# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django.shortcuts import render, redirect
from .forms import CreateUserForm

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("my-login")
        else:
            print(form.errors)

    return render(request, 'signup/register.html', {'registerform': form})




def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data = request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            


    return render(request, 'signup/my-login.html', {'loginform': form})



def dashboard(request):
    return render(request, 'signup/dashboard.html')

def user_logout(request):

    auth.logout(request)

    return redirect("/")