from todo.models import Todo
from django.forms import ModelForm
from django import forms

class TodoForm(ModelForm):
    title = forms.CharField(
                    max_length=100,
                    required=True,
                    help_text='Enter New Task',
                    widget=forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'New Task'}),
                    )
    class Meta:
        model = Todo
        fields = ['title', 'status', 'priority']