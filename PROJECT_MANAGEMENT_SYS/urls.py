from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('app_auth.urls')),
    path('api/', include('app_management.urls')),
]
