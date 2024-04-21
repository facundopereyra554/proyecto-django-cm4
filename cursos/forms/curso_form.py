from ..models import Curso, Instructor, Categoria
from django import forms
from tinymce.widgets import TinyMCE


class CursoForm(forms.ModelForm):

    instructor = forms.ModelChoiceField(
        queryset=Instructor.objects.all(),
        required=False,
        empty_label="Selecione el profesor",
        widget=forms.Select(attrs={"class": "form-control"}),  
    )

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        empty_label="Selecione la categoria",
        widget=forms.Select(attrs={"class": "form-control"}),  
    )


    class Meta:
        model = Curso

        fields = [
            "nombre",
            "descripcion",
            "contenido",
            "precio",
            "fecha_publicacion",
            "instructor",
            "categoria",
            "duracion",
            "estado",
            "destacado",
            "imagen",
        ]
        labels = {
            "nombre": "Nombre del curso",
            "descripcion": "Descripción del curso",
            "precio": "Precio del curso",
            "fecha_publicacion": "Fecha de publicación",
            "instructor": "Profesor",
            "categoria": "Categoría",
            "duracion": "Duración del curso",
            "estado": "Estado del curso",
            "destacado": "Destacado",
            "imagen": "Imagen del curso",
        }

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese nombre del curso",}),
            "descripcion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese descripción del curso",}),
            "contenido": TinyMCE(attrs={"placeholder": "Ingrese el contenido",}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese precio del curso",}),
            "fecha_publicacion": forms.NumberInput(attrs={"class": "form-control", "type": "date", "placeholder": "Ingrese fecha de publicación",}),
            "duracion": forms.TimeInput(attrs={"class": "form-control", "placeholder": "Ingrese duración del curso",}),
            "estado": forms.Select(attrs={"class": "form-control",}),
            "destacado": forms.CheckboxInput(attrs={"class": "form-check-input",}),
            "imagen": forms.FileInput(attrs={"class": "form-control",}),
        }

        