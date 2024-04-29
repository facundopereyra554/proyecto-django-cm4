# Generated by Django 5.0.3 on 2024-04-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cursos", "0008_alter_curso_precio_alter_inscripcion_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="curso",
            name="imagen",
            field=models.ImageField(
                blank=True, default="cursos/fallback.png", upload_to="cursos"
            ),
        ),
        migrations.AddField(
            model_name="estudiante",
            name="avatar",
            field=models.ImageField(
                blank=True, default="estudiantes/fallback.png", upload_to="estudiante"
            ),
        ),
        migrations.AddField(
            model_name="instructor",
            name="avatar",
            field=models.ImageField(
                blank=True, default="instructores/fallback.png", upload_to="instructor"
            ),
        ),
    ]