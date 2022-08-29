# Django
from django.db import models

# Models
from code_challenge.subjects.models import Subjects
from code_challenge.students.models import Students


class Grades(models.Model):
    grade = models.FloatField(verbose_name="Nota", help_text="Ingresa una nota entre 0 y 5")
    description = models.CharField(verbose_name="Descripción", max_length=255)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name="Materia")
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
