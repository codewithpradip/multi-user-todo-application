from django.shortcuts import render, redirect
from todo.forms import TodoForm
from todo.models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='home')
def index(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm()
        todo = Todo.objects.filter(user=user).order_by('priority')
        return render(request, 'core/index.html', {'form':form, 'todo':todo})

@login_required(login_url='home')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()

            return redirect("index")
        else:
            return render(request, 'core/home.html', {'form':form })

def delete_todo(request,id):
    Todo.objects.get(pk=id).delete()
    return redirect('index')

def change_todo_status(request, id, status):
    todo = Todo.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('index')