from rest_framework import serializers
from .models import Task


# This packager allow us to create a serializer model

class TaskSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('id', 'title', 'description', 'done')
        fields = '__all__'