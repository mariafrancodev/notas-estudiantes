from django.db import models


class Subjects(models.Model):
    name = models.CharField("Nombre", blank=True, max_length=255)

    def __str__(self):
        return self.name
