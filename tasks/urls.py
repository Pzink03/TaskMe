from django.urls import path
from tasks.views import create_task, task_list

urlpatterns = [
    path("mine/", task_list, name="show_my_tasks"),
    path("create/", create_task, name="create_task"),
]
