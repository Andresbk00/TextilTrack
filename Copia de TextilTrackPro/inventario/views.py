from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto

@login_required
def lista_inventario(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/inventario_lista.html', {'productos': productos})
