# crud/urls.py
from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    # Páginas principales (obesidad)
    path('', views.obesity_home, name='home'),
    path('causas/', views.obesity_causes, name='causes'),
    path('prevencion/', views.obesity_prevention, name='prevention'),
    path('estadisticas/', views.obesity_statistics, name='statistics'),
    path('consejos/', views.healthy_tips, name='tips'),
    
    # Elimina o comenta las líneas del CRUD antiguo:
    # path('tasks/', views.task_list_and_create, name='task_list'),
    # path('tasks/update/<int:task_id>/', views.update_task, name='update_task'),
    # path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    # path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
