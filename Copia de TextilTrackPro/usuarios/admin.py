from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'rol', 'aprobado', 'fecha_creacion')
    list_filter = ('rol', 'aprobado')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    readonly_fields = ('fecha_creacion',)  # 👈 Esta línea es la clave

    fieldsets = (
        ('Información del usuario', {
            'fields': ('username', 'email', 'first_name', 'last_name', 'password', 'rol', 'aprobado')
        }),
        ('Fechas importantes', {
            'fields': ('last_login', 'fecha_creacion'),
        }),
    )
