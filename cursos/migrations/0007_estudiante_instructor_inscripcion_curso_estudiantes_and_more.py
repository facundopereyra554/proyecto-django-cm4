# Generated by Django 5.0.3 on 2024-03-22 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cursos", "0006_curso_destacado_curso_requisitos_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Estudiante",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Instructor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("bio", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Inscripcion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_inscripcion", models.DateField(auto_now_add=True)),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cursos.curso"
                    ),
                ),
                (
                    "estudiante",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cursos.estudiante",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="curso",
            name="estudiantes",
            field=models.ManyToManyField(
                through="cursos.Inscripcion", to="cursos.estudiante"
            ),
        ),
        migrations.AddField(
            model_name="curso",
            name="instructor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="cursos.instructor",
            ),
        ),
    ]
