from django.urls import path
from .views import *
urlpatterns=[
    path('',home.as_view(),name='home'),
    path('register/',register.as_view(),name='register'),
    path('login/',customer_login.as_view(),name='customer_login'),
    path('logout/',customer_logout.as_view(),name='customer_logout'),
    path('profile/',customer_profile.as_view(),name='customer_profile'),
    path('forget_password/',forget_password.as_view(),name='forget_password'),
    path('otp/',otp.as_view(),name='otp'),
    path('new_password/',new_password.as_view(),name='new_password'),
    path('change_password/',change_password.as_view(),name='change_password'),
]