from django.http import HttpRequest
from django.contrib import messages, auth
from django.shortcuts import redirect
from django.views import View

class LogoutView(View):
    def get(self, request: HttpRequest):
        auth.logout(request)
        messages.success(request, "Vous êtes déconnecté, à bientôt !")
        return redirect("welcome")
