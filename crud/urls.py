from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    # Página Principal
    path('', views.home, name='home'),
    
    # Secciones de Obesidad
    path('causas/', views.procedimiento, name='procedimiento'),
    path('prevencion/', views.prevention, name='prevención'),
    path('estadisticas/', views.obesity_statistics, name='statistics'),
    path('consejos/', views.healthy_tips, name='tips'),
    
    # Eliminar rutas antiguas del CRUD
    # path('tasks/', ...),  # Comenta o elimina estas líneas
]
