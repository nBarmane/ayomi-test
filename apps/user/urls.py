from django.urls import include, path, re_path

from .views import views
from .views.LoginView import LoginView
from .views.WelcomeView import WelcomeView
from .views.UserView import UserView
from .views.LogoutView import LogoutView
from .views.ErrorView import ErrorView

from .views import user_api_views

urlpatterns = [
    path('', WelcomeView.as_view(), name = 'welcome'),
    path('login', LoginView.as_view(), name = 'login'),
    path('user', UserView.as_view(), name = 'user'),
    path('logout', LogoutView.as_view(), name = 'logout'),
    
    path('api/user/update', user_api_views.updateUser, name = 'update_user'),
    
    re_path(r'.*', ErrorView.as_view()),
]
