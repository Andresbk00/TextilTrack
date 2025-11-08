from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

Usuario = get_user_model()

# -------------------------------
# VISTA PRINCIPAL
# -------------------------------
def home_view(request):
    return render(request, 'usuarios/home.html')


# -------------------------------
# LOGIN (por correo electrónico)
# -------------------------------
def web_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(email=email)
            username = user.username  # Django autentica con username internamente
        except Usuario.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos.')
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.aprobado:
                login(request, user)
                if user.rol == 'administrador':
                    return redirect('panel_admin')
                elif user.rol == 'vendedor':
                    return redirect('panel_vendedor')
                elif user.rol == 'auxiliar':
                    return redirect('panel_aux')
                else:
                    return redirect('home')
            else:
                messages.error(request, 'Tu cuenta aún no ha sido aprobada por el administrador.')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')


# -------------------------------
# REGISTRO
# -------------------------------
def web_register(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rol = request.POST.get('rol')

        # Validar formato del correo
        if not email.endswith(('@gmail.com', '@hotmail.com', '@outlook.com', '@yahoo.com')):
            messages.error(request, "Por favor usa un correo válido.")
            return redirect('registro')

        # Validar duplicados
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Este email ya está registrado.")
            return redirect('registro')

        username = email.split('@')[0]

        # Crear usuario inactivo (esperando aprobación)
        usuario = Usuario.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=nombre,
            last_name=apellido,
            rol=rol,
            is_active=False,
            aprobado=False
        )
        usuario.save()

        messages.success(request, "Tu registro fue enviado. Espera la aprobación del administrador.")
        return redirect('login')

    return render(request, 'usuarios/registro.html')


# -------------------------------
# LOGOUT
# -------------------------------
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# -------------------------------
# PANELES POR ROL
# -------------------------------
@login_required
def panel_admin(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/panel_admin.html', {'usuarios': usuarios})


@login_required
@require_POST
def aprobar_usuario(request, user_id):
    if request.user.rol != 'administrador':
        messages.error(request, "No tienes permisos para aprobar usuarios.")
        return redirect('panel_admin')

    try:
        usuario = Usuario.objects.get(id=user_id)
        usuario.aprobado = True
        usuario.is_active = True
        usuario.save()
        messages.success(request, f"Usuario {usuario.username} aprobado correctamente.")
    except Usuario.DoesNotExist:
        messages.error(request, "El usuario no existe.")

    return redirect('panel_admin')


@login_required
@require_POST
def eliminar_usuario(request, user_id):
    if request.user.rol != 'administrador':
        messages.error(request, "No tienes permisos para eliminar usuarios.")
        return redirect('panel_admin')

    try:
        usuario = Usuario.objects.get(id=user_id)
        usuario.delete()
        messages.success(request, f"Usuario {usuario.username} eliminado correctamente.")
    except Usuario.DoesNotExist:
        messages.error(request, "El usuario no existe.")

    return redirect('panel_admin')


@login_required
def panel_vendedor(request):
    return render(request, 'usuarios/panel_vendedor.html')


@login_required
def panel_aux(request):
    return render(request, 'usuarios/panel_aux.html')
