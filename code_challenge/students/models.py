from django.db import models


class Students(models.Model):
    TYPES = (
        ('tarjeta_de_identidad', 'Tarjeta de Identidad'),
        ('cedula', 'Cédula'),
    )
    identification_type = models.CharField(
        "Tipo de documento",
        max_length=32,
        choices=TYPES,
    )
    identification = models.CharField("Número Identificación", max_length=11)
    name = models.CharField("Nombre", max_length=255)
    last_name = models.CharField("Apellido", max_length=255)
    phone_number = models.CharField("Número celular", max_length=20, blank=True, null=True)
