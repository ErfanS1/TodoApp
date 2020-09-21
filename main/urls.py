from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('open_task/<int:task_id>', views.open_task, name='open_task'),
    path('close_task/<int:task_id>', views.close_task, name='close_task'),
]