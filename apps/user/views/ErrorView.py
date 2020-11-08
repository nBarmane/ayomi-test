from django.http import HttpRequest
from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

class ErrorView(View):
    def get(self, request: HttpRequest):
        messages.warning(request, "La page demandée n'existe pas, vous avez été redirigé.")
        return redirect("welcome")
