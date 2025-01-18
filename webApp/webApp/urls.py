from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('sessionLogger.urls')), 
    path('', include('tasks.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth views
    path('accounts/two_factor/', include('two_factor.urls')),  # Correct two_factor path
    path('admin/', admin.site.urls),  # Admin panel
]
