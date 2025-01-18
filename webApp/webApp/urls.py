from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('sessionLogger.urls')), 
    path('tasks/', include('tasks.urls')), 

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth URLs for authentication
]
