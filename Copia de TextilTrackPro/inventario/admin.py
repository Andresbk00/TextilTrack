from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'cantidad', 'fecha_ingreso', 'registrado_por')
    list_filter = ('categoria', 'fecha_ingreso')
    search_fields = ('nombre',)
