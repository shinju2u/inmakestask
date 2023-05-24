from django.contrib import admin
from django.urls import path, include

from storeapp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
path('product/', views.product, name='product'),

]

