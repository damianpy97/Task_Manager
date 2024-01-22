from django.forms import ModelForm
from .models import Task, History

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [ 'id','name', 'user', 'status', 'description']

class HistoryTaskForm(ModelForm):
    class Meta:
        model = History
        fields = '__all__'