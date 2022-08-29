# Django
from django import forms
from django.core.exceptions import ValidationError

# Models
from .models import Students


class StudentForm(forms.ModelForm):
    def clean_identification(self):
        identification = self.cleaned_data["identification"]
        if Students.objects.filter(identification__icontains=identification).exists():
            raise ValidationError("Ya existe un estudiante con esa identificación.")
        return identification

    class Meta:
        model = Students
        fields = ('identification_type', 'identification', 'name', 'last_name', 'phone_number')
