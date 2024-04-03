from django.urls import path
from .views import home, curso_list, curso_detail


urlpatterns = [
    path("", home, name="home"),
    path("cursos/", curso_list, name="curso_list"),
    path("cursos/<int:curso_id>/", curso_detail, name="curso_detail"),
]