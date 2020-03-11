from django import forms
from .models import *

def widget_attrs(placeholder):
    return {'class':'input-wrap','placeholder': placeholder}


def form_kwargs(widget, label='', max_length=128):
    return {'widget': widget, 'label': label, 'max_length': max_length}



class TodoListForm(forms.Form):
    title = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(attrs=widget_attrs('Enter your todo name')),
            label="Title"
        )
        
    )
    description =  forms.CharField()
    target_time = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )
  
  
class TodoForm(forms.ModelForm):
   class Meta:
       model = Todo
       fields = ['title','description'] 