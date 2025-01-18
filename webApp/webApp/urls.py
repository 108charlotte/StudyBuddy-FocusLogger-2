from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', include('sessionLogger.urls')), 
    path('', include('tasks.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/two_factor/', include('two_factor.urls')),  # Corrected
    path('admin/', admin.site.urls),
]
