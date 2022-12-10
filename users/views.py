from django.shortcuts import render, redirect, reverse
from django.views import View
from . import forms
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class LoginView(View):

    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})
