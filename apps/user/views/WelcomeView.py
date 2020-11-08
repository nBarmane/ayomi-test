from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

class WelcomeView(View):
    template_name = 'welcome.html'

    def get(self, request: HttpRequest):
        return render(request, self.template_name)
