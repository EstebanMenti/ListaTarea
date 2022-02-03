from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

import datetime

from .forms import TareasForm
from .models import Tareas

# Create your views here.
@login_required
def get_tareas(request): 
    tareas = Tareas.objects.filter( user_id = request.user.id )
    #tareas = Tareas.objects.filter(nombre__icontains=user_id)
    error = False
    
    # if this is a POST request we need to process the form data
    if( request.method == 'POST'):
        new_tarea = Tareas(user_id = request.user.id)

        # create a form instance and populate it with data from the request:
        form = TareasForm( request.POST, instance=new_tarea )
        # check whether it's valid:
        if( form.is_valid() ):
            form.save()

        else:
            error = True
    # if a GET (or any other method) we'll create a blank form
    else:
       #form = TareasForm(initial={'user_id': 'user'})
       form = TareasForm()

    return render( request, 'tareas_list.html',
            context={'tareas': tareas,
                     'now': datetime.datetime.now(),
                     'form': form,
                     'error':error})

# Create your views here.
@login_required
def tarea_detalle(request, id_tarea):
    tarea = Tareas.objects.get(pk=id_tarea)
    form = TareasForm( instance=tarea )
    
    if( request.method == 'POST'):
        form = TareasForm(request.POST, instance = tarea)
        if( form.is_valid()):
            form.save(commit=True)
    
    return render(request, 'tarea_detalle.html',
            context={'tarea': tarea,
                     'item': id_tarea,
                     'form': form})


def tarea_clear(request, id_tarea):
    Tareas.objects.get(pk=id_tarea).delete()    
    return redirect('/tareas')