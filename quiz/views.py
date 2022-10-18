from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic

from .forms import LoginForm, RegisterForm
from .models import User

# Create your views here.
class IndexView(generic.View):

    def get(self, request):
        context = {"form": LoginForm()}
        return render(request, "index.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        context = {"form": form}
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.check_username(username) and User.check_password(password):
            ...
        
        else:
            form.add_error("username", "Incorrect username or password")
            return render(request, "index.html", context)



class RegisterView(generic.View):
    
    def get(self, request):
        context = {"form": RegisterForm()}
        return render(request, "register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)
        context = {"form": form}
        
        name = request.POST.get("name")
        user = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if User.check_name(name):
            form.add_error("name", "Name already exists")

        if User.check_username(user):
            form.add_error("username", "Username already exists")

        if password != confirm_password:
            form.add_error("confirm_password", "Confirm password must match the password")

        if form.errors:
            return render(request, "register.html", context)

        return "Register success"
    

class QuizPageView(generic.View):
    ...