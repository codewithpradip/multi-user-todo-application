from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
    path('change_todo_status/<int:id>/<str:status>', views.change_todo_status, name='change_todo_status')

]