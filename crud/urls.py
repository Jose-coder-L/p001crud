from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    # Página Principal
    path('', views.home, name='home'),
    
    # Secciones de Obesidad
    path('procedimiento/', views.procedimiento, name='procedimiento'),
    path('prevencion/', views.prevention, name='prevención'),
  
    
    # Eliminar rutas antiguas del CRUD
    # path('tasks/', ...),  # Comenta o elimina estas líneas
]
