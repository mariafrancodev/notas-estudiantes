# Django
from django import forms
from django.core.exceptions import ValidationError

# Models
from .models import Subjects


class SubjectsForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if Subjects.objects.filter(name__icontains=name).exists():
            raise ValidationError("Ya existe una materia con ese nombre.")
        return name

    class Meta:
        model = Subjects
        fields = ('name', )
