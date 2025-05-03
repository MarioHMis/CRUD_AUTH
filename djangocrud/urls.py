from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('django.contrib.auth.urls')),
    path('tasks/', include('apps.tasks.urls')),
    path('', include('apps.core.urls')),
    path('accounts/', include('apps.accounts.urls')),
]
