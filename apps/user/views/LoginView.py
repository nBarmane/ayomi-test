from django.http import HttpRequest
from apps.user.forms import LoginForm
from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User

class LoginView(View):
    LoginFormClass = LoginForm
    template_name = 'login.html'

    def get(self, request: HttpRequest):
        login_form = self.LoginFormClass()

        if request.user.is_authenticated:
            messages.info(request, "Vous êtes déjà connecté.")
            return redirect("user")

        return render(request, self.template_name, {"form": login_form})
    
    def post(self, request: HttpRequest):
        login_form : LoginForm = self.LoginFormClass(request.POST)

        if login_form.is_valid():
            user : User = auth.authenticate(request, username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, f"Bienvenue {user.first_name}, vous êtes connecté.")
                return redirect("user")
            else:
                messages.error(request, "L'identifiant ou le mot de passe est incorrect.")
        else:
            messages.error(request, "Veuillez saisir des valeurs valides.")
        
        return render(request, self.template_name, {"form": login_form})
