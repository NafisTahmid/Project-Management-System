from django.urls import path
from app_management import views
app_name = 'app_management'

urlpatterns = [
    path('projects/', views.home, name="home")
]