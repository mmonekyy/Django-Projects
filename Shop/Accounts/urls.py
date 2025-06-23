from django.contrib import admin
from django.urls import path 
from Accounts.views import user_register , user_login , accounts_page
urlpatterns = [
    path('', accounts_page, name='accounts'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
]
