# Code Challenge

Programa para subir notas de los estudiantes.

**Nota:** Luego de registrar un usuario debe dirigirse al `localhost:8025` para confirmar el email del usuario registrado.

#### Plantilla:

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

## Tecnologías

* Django
* PostgresSQL
* Docker
* Docker-compose
* Bootstrap
* MailHog

## Módulos

### User
`http://localhost:8000/users/<email>/` Muestra el perfil del admin logueado

`http://localhost:8000/accounts/logout/` Interfaz para cerrar sesión


### Students
`http://localhost:8000/students/` Muestra la lista de estudiantes

`http://localhost:8000/students/<pk>/update` Edita un estudiante

`http://localhost:8000/students/create` Agrega un estudiante

### Subjects (Materias)
`http://localhost:8000/subjects/` Muestra la lista de materias

`http://localhost:8000/subjects/<pk>/update` Edita una materia

`http://localhost:8000/subjects/create` Crea una materia

### Grades (Notas)
`http://localhost:8000/grades/students/<pk>/` Muestra la lista de notas de un estudiante

`http://localhost:8000/grades/<pk>/update/` Edita la nota de un estudiante

`http://localhost:8000/grades/students/<pk>/create/` Agrega una nota a un estudiante

## Comandos
- Para instalar las dependencias:

        $ docker-compose -f local.yml build


- Para correr el proyecto:

        $ docker-compose -f local.yml up

- Para parar el proyecto:

        $ docker-compose -f local.yml down

