from ..models import Curso, Instructor, Categoria
from django import forms


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
            "precio",
            "fecha_publicacion",
            "instructor",
            "categoria",
            "duracion",
            "estado",
            "destacado",
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
        }

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese nombre del curso",}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Ingrese descripción del curso",}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese precio del curso",}),
            "fecha_publicacion": forms.NumberInput(attrs={"class": "form-control", "type": "date", "placeholder": "Ingrese fecha de publicación",}),
            "duracion": forms.TimeInput(attrs={"class": "form-control", "placeholder": "Ingrese duración del curso",}),
            "estado": forms.Select(attrs={"class": "form-control",}),
            "destacado": forms.CheckboxInput(attrs={"class": "form-check-input",}),
        }

        