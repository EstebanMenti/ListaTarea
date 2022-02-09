from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import get_tareas, tarea_detalle, tarea_clear, tarealistView


urlpatterns = [
    path('<int:id_tarea>/',tarea_detalle, name='tareas_detalle'),  #id/<int:id_alumno>/
    path('clear/<int:id_tarea>/',tarea_clear, name='tareas_clear'),
    path('', login_required(tarealistView.as_view()), name='tareas_list'),
]