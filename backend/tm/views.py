from django import views
from .serializer import TodoSerializer
from .models import Todo
from rest_framework import viewsets

# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
