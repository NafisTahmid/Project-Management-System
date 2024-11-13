from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_projects")
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'projects'

class ProjectMembers(models.Model):
    role_choices = [
        ('Admin','Admin'),
        ('Member','Member')   
    ]
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="project_members")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_project_members")
    role = models.CharField(max_length=10,choices=role_choices, default="Member")

    class Meta:
        db_table = 'project_members'


class Tasks(models.Model):
    status_choice = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    ]
    priority_choice = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=status_choice, default="To Do")
    priority = models.CharField(max_length=6, choices=priority_choice, default="Medium")
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="user_tasks")
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="project_tasks")
    created_at = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField(blank=True, null=True)

    
    def __str__(self):
        return self.title[0:50]
    
    class Meta:
        db_table = 'tasks'


class Comments(models.Model):
    content = models.TextField(blank = True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name="task_comments")
    created_at = models.DateTimeField(auto_now_add = True)

    
    def __str__(self):
        return self.content[0:50]
    
    class Meta:
        db_table = 'comments'