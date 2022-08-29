# Django
from django import forms
from django.core.exceptions import ValidationError

# Models
from .models import Grades


class GradeForm(forms.ModelForm):
    def clean_grade(self):
        grade = self.cleaned_data["grade"]
        if not 0 <= grade <= 5:
            raise ValidationError("La nota debe ser entre 0 y 5")
        return grade

    class Meta:
        model = Grades
        fields = ('grade', 'subject', 'description')
