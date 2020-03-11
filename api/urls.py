from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

app_name = 'api'
urlpatterns = [
    path('list/<int:list_id>/', todolistView.as_view(), name='todolist_view')
]
