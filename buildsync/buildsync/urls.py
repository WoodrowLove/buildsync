
from django.contrib import admin
from django.urls import path, include
from pages.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', home, name='home'),
]
