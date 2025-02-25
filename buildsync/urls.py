
from django.contrib import admin
from django.urls import path, include
from pages.views import home

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
    path('contractors/', include('contractors.urls')),
    path('users/', include('users.urls')),
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
