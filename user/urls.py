from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('signup/', views.user_signup, name='user_signup'),
    path('logout/', views.user_logout, name='user_logout'),
]