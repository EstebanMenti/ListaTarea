import pytest 
import uuid
from datetime import datetime, timezone

from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Tareas



@pytest.fixture
def test_password():
    return 'strong-test-password'

@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if('username' not in kwargs):
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return(make_user)

@pytest.fixture
def create_tarea():
    tarea = Tareas.objects.create(
        name="Nombre",
        user_id=id_user,
        descripcion='Descripcion',
        comentarios='Algun comentario',
        status = 'T',
        date_expiration=str(datetime.now(timezone.utc).astimezone())
        )
    tarea.save()
    return Tareas.objects.all().count()

#---- Test de redireccionamiento por no estar logeado -----
@pytest.mark.django_db
def test_tarea_lista_url_unlogin(client):
    url = reverse("tareas_list")
    response = client.get(url)
    assert response.status_code == 302

#---- Test respuesta por estar logeado ----
@pytest.mark.django_db
def test_tarea_lista_url_login(client, test_password, create_user):
    user = create_user()
    url = reverse("tareas_list")
    client.login(
        username = user.username,
        password = test_password
    )
    response = client.get(url)
    assert response.status_code == 200

#---- Test crea una tarea en la DB ----
@pytest.mark.django_db
def test_add_tarea(create_tarea):
    create_tarea
    assert Tareas.objects.all().count() == 1

    