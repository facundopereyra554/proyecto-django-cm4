# Generated by Django 5.0.3 on 2024-04-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cursos", "0009_curso_imagen_estudiante_avatar_instructor_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="estudiante",
            name="avatar",
            field=models.ImageField(
                blank=True, default="estudiantes/fallback.png", upload_to="estudiantes"
            ),
        ),
        migrations.AlterField(
            model_name="instructor",
            name="avatar",
            field=models.ImageField(
                blank=True,
                default="instructores/fallback.png",
                upload_to="instructores",
            ),
        ),
    ]
