from django.contrib.auth.models import AbstractUser
from django.db import models

# 🔑 Opciones de roles
ROLES = [
    ('administrador', 'Administrador'),
    ('vendedor', 'Vendedor'),
    ('auxiliar', 'Auxiliar de Inventario'),
]

class Usuario(AbstractUser):
    rol = models.CharField(max_length=20, choices=ROLES, default='vendedor')
    aprobado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.rol})"
