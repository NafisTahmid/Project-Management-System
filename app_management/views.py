from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from app_management.models import Projects, Tasks
from app_management.forms import CreateProjectForm, CreateTaskForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from app_management.models import Projects

# Create your views here.
def home(request):
    return render(request, 'app_management/home.html', context={})

class ProjectsList(ListView, LoginRequiredMixin):
    model = Projects
    context_object_name = "projects"
    template_name = "app_management/all_projects.html"


@login_required
def create_project(request):
    form = CreateProjectForm()
    if request.method == 'POST':
        form = CreateProjectForm(data = request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return HttpResponseRedirect(reverse('app_management:home'))
    return render(request, 'app_management/create_project.html', {'form':form})

class ProjectDetails(DetailView, LoginRequiredMixin):
    model = Projects
    context_object_name = "project"
    template_name = "app_management/project_details.html"

@login_required
def update_project(request, pk):
    project = Projects.objects.get(pk=pk)
    form = CreateProjectForm(instance = project)
    if request.method == 'POST':
        form =CreateProjectForm(data=request.POST, instance=project)
        if form.is_valid():
            project_object = form.save(commit=False)
            project_object.owner = request.user
            project_object.save()
            return HttpResponseRedirect(reverse('app_management:update_project', kwargs={'pk':pk}))
    return render(request, 'app_management/update_project.html', {'form':form})

@login_required
def delete_project(request, pk):
    project = Projects.objects.get(pk=pk)
    if project is not None:
        project.delete()
        return HttpResponseRedirect(reverse('app_management:home'))
    

# Task section
@login_required
def create_task(request, pk):
    project_object = Projects.objects.get(pk=pk)
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(data = request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project_object
            task.assigned_to = request.user
            task.save()
            return HttpResponseRedirect(reverse('app_management:all_projects'))
    return render(request, 'app_management/create_task.html', context={'form':form})

class ListAllTasks(ListView, LoginRequiredMixin):
    model = Tasks
    context_object_name = "tasks"
    template_name = "app_management/project_details.html"
    
class TaskDetails(DetailView, LoginRequiredMixin):
    model = Tasks
    context_object_name = "task"
    template_name = "app_management/task_details.html"


@login_required
def update_task(request, pk, project_pk):
    task_object = Tasks.objects.get(pk=pk)
    project_object = Projects.objects.get(pk=project_pk)
    form = CreateTaskForm(instance = task_object)
    if request.method == 'POST':
        form = CreateTaskForm(data=request.POST, instance = task_object)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project_object
            task.assigned_to = request.user
            task.save()
            return HttpResponseRedirect(reverse('app_management:project_details', kwargs={'pk':project_pk}))
    return render(request, 'app_management/update_task.html', context={'form':form})

@login_required
def delete_task(request, pk):
    task = Tasks.objects.get(pk=pk)
    if task is not None:
        task.delete()
        return HttpResponseRedirect(reverse('app_management:home'))
