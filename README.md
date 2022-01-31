Introducción
Con el objetivo de poder completar el curso y contar con la experiencia necesaria para
poder desarrollar una aplicación web de punta a punta el ejercicio final consiste en
desarrollar completamente un Sistema utilizando todo lo que aprendieron en en el curso.

Sistema (ToDo: List)
El ejercicio final consiste en desarrollar un sistema de gestion de listas de tareas.
La idea es que el sistema permita:
● Que el usuario tenga una lista individual y única (Lista que solo el usuario logueado
puede ver y no compartirlo con otros usuarios).
● Crear, modificar y eliminar las tareas de dicha lista.
● Las tareas deben tener un estado (Se recomiendo inicialmente: “Todo”, “In
Progress”, “Done” y “Close”)
● La lista de tareas tiene que poder filtrarse por estados, descripción y nombre.
● Las tareas tiene que tener la capacidad de poder configurar una fecha de
vencimiento, la idea es que en el listado se agregue algún elemento visual que de a
entender cuales son las tareas que están vencidas.-
Detalle de tareas:
● Desde la lista de tareas, se debe poder acceder al detalle de la tarea
● En el detalle se debe poder modificar, actualizar y agregar comentarios.

Flujo normal de uso:
1. Usuario X se registra/loguea para ingresar al sistema
2. Accede a la lista de tareas propias.
a. Crea Tareas:
i. Ingresa a formulario de creación de tareas
ii. Ingresa al detalle de la tarea
iii. Vuelve a la lista de tareas
b. Ingresa a detalle de una tarea en uso
i. Hace click en la lista y va al detalle de la tarea para gestionarla
ii. Edita, lee, carga avances, etc.
iii. Vuelve a la lista de tareas
c. Filtrar las tareas de la lista
i. Desde la lista de tareas puede filtrar, tareas para ver detalles
especificos.-

Notas Generales:
● Para desarrollar el front-end se recomienda usar el framework que les sea más
cómodo no es necesario usar uno en particular.-
● Al momento de desarrollar la solución usar las herramientas aprendidas en el curso.
○ Docker: Usar los conocimientos aprendidos y procedimientos generales (se
puede hacer uso de los templates del curso)
○ Github: se solicita usar lo aprendido en github, subiendo todo a repositorio e
implementar el uso de Git Flow, PR, etc para ordenar el desarrollo.
● Se permite colaborar cruzadamente entre alumnos o realizar consultas al profesor
en el proceso.
● Recuerden poder aprovechar e incorporar el máximo de contenido adquirido en el
curso, no sera motivo de rechazo no usar todo, pero a major y mejores
implementaciones se le sumara mas puntaje.-


docker exec -i -t 80d760f73633 /bin/bash