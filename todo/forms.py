from django import forms

from todo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta():
        model = Todo

        fields = (
            'title',
            'description',
            'limit',
        )
        
        labels = {
            'title':'タイトル',
            'description':'説明',
            'limit':'締切日'
        }