from django.shortcuts import render, redirect
from todo.forms import TodoForm
# Create your views here.

def home(request):
    form = TodoForm()
    return render(request, 'core/home.html', {'form':form })
