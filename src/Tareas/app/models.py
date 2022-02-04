from django.db import models

class Tareas(models.Model):
    STATUS_CHOINES = (
        ('T', 'Todo'),
        ('P', 'In Progress'),
        ('D','Done'),
        ('C','Close'),
    )
    name = models.CharField(max_length=200)
    
    user_id = models.IntegerField()
    descripcion = models.CharField('Descripcion', max_length=200 )
    comentarios = models.CharField('Comentario', max_length=200 )
    status = models.CharField('Estado', max_length=4, choices = STATUS_CHOINES,
                               default='T', blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField('EXPIRA',null=True)
    date_update = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return f'{self.name.title()}, {self.status.title()}'

