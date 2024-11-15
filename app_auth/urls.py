from django.urls import path
from app_auth import views
app_name = 'app_auth'

urlpatterns = [
    path('register/', views.registration, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('users/<pk>/', views.update_user, name="update_user"),
    path('user-details/<pk>/', views.user_details, name="user_details"),
    path('delete-user/<pk>/', views.delete_user, name="delete_user"),
    path('change_password/', views.change_password, name="change_password")
]
