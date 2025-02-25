from django.urls import path
from .views import contractor_list, contractor_detail, contractor_create, contractor_update, contractor_delete

urlpatterns = [
    path('', contractor_list, name='contractor_list'),
    path('<int:pk>/', contractor_detail, name='contractor_detail'),
    path('create/', contractor_create, name='contractor_create'),
    path('<int:pk>/edit/', contractor_update, name='contractor_update'),
    path('<int:pk>/delete/', contractor_delete, name='contractor_delete'),
]