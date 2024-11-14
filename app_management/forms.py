from django import forms
from app_management.models import Projects, Tasks

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ('owner', )


class CreateTaskForm(forms.ModelForm):
    
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Tasks
        exclude = ('assigned_to', 'project', )