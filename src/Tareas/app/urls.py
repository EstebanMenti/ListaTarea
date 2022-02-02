from django.urls import path

from .views import get_tareas, tarea_detalle, tarea_clear


urlpatterns = [
    path('', get_tareas, name="get-tarea"),
    #path('tarea', add_tarea),
    path('<int:id_tarea>/',tarea_detalle),  #id/<int:id_alumno>/
    path('clear/<int:id_tarea>/',tarea_clear),
]