from django.db import models
from usuarios.models import Usuario
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    registrado_por = models.ForeignKey(
        Usuario, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='producto'
    )

    def __str__(self):
        return f"{self.nombre} - {self.categoria.nombre}"


class EntradaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_entrada = models.DateTimeField(default=timezone.now)
    registrado_por = models.ForeignKey(
        Usuario, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='entradas_registradas'
    )

    def __str__(self):
        return f"Entrada de {self.cantidad} {self.producto.nombre}"


class SalidaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_salida = models.DateTimeField(default=timezone.now)
    registrado_por = models.ForeignKey(
        Usuario, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='salidas_registradas'
    )

    def __str__(self):
        return f"Salida de {self.cantidad} {self.producto.nombre}"
