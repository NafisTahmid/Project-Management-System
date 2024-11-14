from django.urls import path
from app_management import views
app_name = 'app_management'

urlpatterns = [
    path('home/', views.home, name="home"),
    path('projects/', views.ProjectsList.as_view(), name="all_projects"),
    path('create-project', views.create_project, name="create_project"),
    path('project-details/<pk>', views.ProjectDetails.as_view(), name="project_details"),
    path('update-project/<pk>', views.update_project, name="update_project"),
    path('delete-project/<pk>', views.delete_project, name="delete_project"),
    path('create-task/<pk>', views.create_task, name="create_task"),
    path('tasks/',views.ListAllTasks.as_view(), name="all_tasks"),
    path('task-details/<pk>', views.TaskDetails.as_view(), name="task_details"),
    path('update-task/<int:project_pk>/<int:pk>/', views.update_task, name="update_task"),
    path('delete-task/<pk>', views.delete_task, name="delete_task")
]