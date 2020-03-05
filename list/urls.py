from django.urls import path

from .views import *

app_name = 'list'
urlpatterns = [
    path('', todocreateView.as_view(), name='index'),
    
    path('todolist', todoList.as_view(), name='todolist'),
]
