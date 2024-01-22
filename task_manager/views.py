from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task, History
from .forms import TaskForm, HistoryTaskForm
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, LogoutView
from .filters import *
from rest_framework.authentication import TokenAuthentication
from django.views.generic.list import ListView
from django.contrib.auth.models import Group, User
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.decorators import action
from rest_framework.mixins import *
from .serializers import *
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .models import History


class TMLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True


def custom_logout(request):
    logout(request)
    return redirect("login")


def custom_login(request):
    login(request)
    return redirect("all")


# def all_tasks(request):
#     all = Task.objects.all()
#     myFilter = TaskFilter(request.GET, queryset=all)
#     all = myFilter.qs
#     return render(request, 'tasks.html', {'all': all, 'myFilter': myFilter})

# def create_task(request):
#     form = TaskForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     serializer = TaskSerializer
#     return render(request, 'create_task.html', {'form': form})

class TaskView(viewsets.ReadOnlyModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'status', 'user']
    filterset_class = TaskFilter

    # def get_queryset(self):
    #     tasks = Task.objects.all()
    #     return tasks

    # def list(self, request, *args, **kwargs):
    #     queryset = self.queryset
    #     serializer = TaskSerializer(self.queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     task = Task.objects.create(name=request.data['name'],
    #                                description=request.data['description'],
    #                                status=request.data['status'],
    #                                user=request.data['user'])
    #     serializer = TaskSerializer(task, many=False)
    #     return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = TaskSerializer(instance)
    #     return Response(serializer.data)
    #
    # def destroy(self,request, *args, **kwargs):
    #     task = self.get_object()
    #     task.delete()
    #     return Response('usuniety')


class TaskDetail(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # def retrieve(self, request, pk=None):
    #     queryset = Task.objects.all()
    #     instance = self.get_object()
    #     t = get_object_or_404(queryset, pk=pk)
    #     serializer = TaskSerializer(t)
    #     return Response(serializer.data)


class UpdateTask(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# def delete_task(request, id):
#     task = get_object_or_404(Task, pk=id)
#     if request.method == 'POST':
#         task.delete()
#         return redirect(all_tasks)
#     return render(request, 'confirm.html', {'form': task})

# def task_detail(request, id):
#     task = get_object_or_404(Task, pk=id)
#     return render(request, 'task_details.html', {'task': task})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoryFilter


def filtr(request):
    filter_queryset = History.objects.all()
    his_filter = HistoryFilter(request.GET, queryset=filter_queryset)
    filter_queryset = his_filter.qs
    return render(request, 'history.html', {'filter_queryset': filter_queryset, 'his_filter': his_filter})

# class ProbaHistoryViewSet(viewsets.ModelViewSet):  # or PollHistorySerializer(ModelSerializer):
#     queryset = HistoricalProba.objects.all()
#     serializer_class = HistoricalProbaSerializer
#     permission_classes = [permissions.IsAuthenticated]

