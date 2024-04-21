from django.urls import path
from .views import (
    curso_list,
    curso_detail,
    home,
    create_curso,
    update_curso,
    delete_curso,
    curso_list_archive,
    curso_archive,
    curso_restore
)


urlpatterns = [
    path("", home, name="home"),
    path("cursos/", curso_list, name="curso_list"),
    path("cursos/<int:curso_id>/", curso_detail, name="curso_detail"),
    path("cursos/crear/", create_curso, name="curso_create"),
    path("cursos/<int:curso_id>/actualizar/", update_curso, name="curso_update"),
    path("cursos/<int:curso_id>/eliminar/", delete_curso, name="curso_delete"),
    path("cursos/archivados", curso_list_archive, name="curso_list_archive"),
    path("cursos/<int:curso_id>/archivar", curso_archive, name="curso_archive"),
    path("cursos/<int:curso_id>/restaurar", curso_restore, name="curso_restore"),
]