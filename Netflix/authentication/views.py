from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')  # Redirige al home después de iniciar sesión
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'authentication/login.html', {
        'hide_login_button': True,  # Oculta el botón "Iniciar Sesión"
        'show_register_button': True  # Muestra el botón "Registrarse"
    })


def user_logout(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya está registrado.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
                return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')

    return render(request, 'authentication/register.html', {'show_register_button': False})