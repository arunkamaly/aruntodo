from django.urls import path

from .views import *

app_name = 'list'
urlpatterns = [
    path('', todocreateView.as_view(), name='index'),
    
    path('todolist', todoList.as_view(), name='todolist'),
    path('finishedtodolist', finishedtodoList.as_view(), name='finishedtodolist'),
    
    path('todoedit/<pk>/', todoEdit.as_view(), name='edit_todo'),
    path('tododelete/<pk>/', todoDelete.as_view(), name='delete_todo'),
]
