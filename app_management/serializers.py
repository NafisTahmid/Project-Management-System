from rest_framework import serializers
from .models import Projects, ProjectMembers, Tasks, Comments

# Serializer for Projects model
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'description', 'owner', 'created_at']

# Serializer for ProjectMembers model
class ProjectMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembers
        fields = ['id', 'project', 'user', 'role']

# Serializer for Tasks model
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id', 'title', 'description', 'status', 'priority', 
            'assigned_to', 'project', 'created_at', 'due_date'
        ]

# Serializer for Comments model
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'content', 'user', 'task', 'created_at']
