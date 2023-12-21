from django.urls import path
from .views import *


urlpatterns = [

    path('', homepage, name="homepage"),
    path('register', register, name="register"),
    path('my-login', my_login, name="my-login"),
    path('dashboard', dashboard, name="dashboard"),
    path('user-logout', user_logout, name="user-logout"),


]
