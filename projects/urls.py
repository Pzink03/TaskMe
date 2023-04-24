from django.urls import path
from projects.views import project_list, show_projects, create_project

urlpatterns = [
    path("create/", create_project, name="create_project"),
    path("", project_list, name="list_projects"),
    path("<int:id>/", show_projects, name="show_project"),
]
