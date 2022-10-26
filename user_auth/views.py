from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import generic

from .forms import LoginForm, RegisterForm

# Create your views here.
class LoginView(generic.View):
    template_name = "login.html"

    def get(self, request):
        context = {"form": LoginForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        context = {"form": form}

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")

        form.add_error("username", "Incorrect username or password")
        return render(request, self.template_name, context)


class RegisterView(generic.View):
    template_name = "register.html"

    def get(self, request):
        context = {"form": RegisterForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)
        context = {"form": form}

        if form.is_valid():
            form.save()
            return redirect("login")

        return render(request, self.template_name, context)


class LogoutView(generic.View):

    def get(self, request):
        logout(request)
        return redirect("login")