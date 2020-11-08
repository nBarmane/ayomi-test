from django.http import HttpRequest
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

class UserView(View):
    template_name = 'user-info.html'

    def get(self, request: HttpRequest):
        if not request.user.is_authenticated:
            return redirect("login")
        
        return render(request, self.template_name)
