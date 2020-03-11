from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from django.views.generic import TemplateView, ListView, CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TodoListForm,TodoForm
from .models import *
import pdb
import random
import string
import json

class todocreateView(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'list/index.html', {'form': TodoListForm()})

    def post(self, request, *args, **kwargs):
        form = TodoListForm(request.POST)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None
            todo = Todo(
                title=request.POST['title'],
                description=request.POST['description'],
                target_at=request.POST['target_time'],
                creator=user
            )
            todo.save()
            return redirect('list:todolist')
        else:
            print("unvalid")
   
        return redirect('list:index')

class todoList(LoginRequiredMixin, ListView):
    context_object_name = 'lists'
    # queryset = Todo.objects.filter(is_finished=False,creator=request.user)
    template_name = 'list/lists.html'
    
    def get_queryset(self):
        return Todo.objects.filter(is_finished=False,creator=self.request.user)
    
    
class finishedtodoList(LoginRequiredMixin ,ListView):
    context_object_name = 'lists'
    template_name = 'list/finishedlists.html'
    
    def get_queryset(self):
        return Todo.objects.filter(is_finished=True,creator=self.request.user)
    
    
class todoEdit(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title','description','target_at','is_finished']
    template_name = 'list/edit_todo.html'
    success_url = reverse_lazy('list:todolist')
    
class todoDelete(DeleteView): 
    model = Todo
    success_url = reverse_lazy('list:todolist')
