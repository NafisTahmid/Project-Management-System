from django.db import models

from django.contrib.auth.models import User

# Create your models here.
# class Users(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="project_users")
#     email = models.EmailField(max_length=200, blank=True, unique=True)
#     password = models.CharField(max_length=200, blank=True)
#     first_name = models.CharField(max_length=200, blank=True)
#     last_name = models.CharField(max_length=200, blank=True)
#     date_joined = models.DateField(blank=True, auto_now_add = True)

#     def __str__(self):
#         return self.first_name