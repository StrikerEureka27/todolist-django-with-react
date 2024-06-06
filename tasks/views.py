from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TaskSeriallizer
from .models import Task
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSeriallizer
    queryset = Task.objects.all()


