# task_management_system/urls.py

from django.contrib import admin
from django.urls import include, path
from tasks.views import UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Your app's URL configuration
    path('accounts/login/', UserLoginView.as_view(), name='user_login'),  # Custom login view
    path('accounts/', include('django.contrib.auth.urls')),  # Default auth URLs for password reset
]

