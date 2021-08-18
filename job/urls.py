from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register, company

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(
        template_name='company/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='company/logout.html'
    ), name='logout'),
    path('company/', company, name='company')
]