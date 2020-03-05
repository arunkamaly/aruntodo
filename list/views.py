from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from django.views.generic import TemplateView, ListView, CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
import pdb
import random
import string
import json
from .forms import TodoListForm
from .models import *

class todocreateView(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'list/index.html', {'form': TodoListForm()})

    def post(self, request, *args, **kwargs):
        form = TodoListForm(request.POST)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None
            todo = Todo(
                title=request.POST['title'],
                description=request.POST['description'],
                target_at=request.POST['finished_at'],
                creator=user
            )
            todo.save()
            return redirect('list:todolist')
        else:
            print("unvalid")
   
        return redirect('list:index')

class todoList(ListView):
    context_object_name = 'lists'
    queryset = Todo.objects.all()
    template_name = 'list/lists.html'