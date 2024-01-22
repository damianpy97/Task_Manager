from django.urls import path, include
from task_manager.views import *
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'history', views.HistoryViewSet)
router.register(r'task_list', views.TaskView)

urlpatterns = [

    path('create/', CreateTask.as_view(), name="create"),
    path('update/<int:pk>/', UpdateTask.as_view(), name="edit"),
    path('delete/<int:pk>/', DeleteTask.as_view(), name="delete"),
    path('task_detail/<int:pk>/', UpdateTask.as_view(), name="task_detail"),
    path('login/', TMLoginView.as_view(), name="login"),
    path('logout/', views.custom_logout, name='logout'),
]

urlpatterns += router.urls