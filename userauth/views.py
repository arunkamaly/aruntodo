from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import CreateView

from userauth.forms import LoginForm, RegistrationForm

class loginView(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'userauth/login.html', {'form': LoginForm()})
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=request.POST['username'],
                    password=request.POST['password']
                )
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('list:index')
            else:
                return render(request, 'userauth/login.html', {'form': LoginForm(),"error":"Incorrect username and/or password."})
        else:
            return render(request, 'userauth/login.html', {'form': LoginForm()})



class registerView(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'userauth/register.html', {'form': RegistrationForm()})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password']
                )
                return redirect('userauth:login')
            except:
                print(form)
                return render(request, 'userauth/register.html', {'form': form})
        else:
            return render(request, 'userauth/register.html', {'form': form})


class logoutView(CreateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('list:index')

