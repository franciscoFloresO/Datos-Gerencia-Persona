from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from usuario.backends import UsuarioBackend

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            messages.error(request, 'Por favor ingresa un correo electrónico y una contraseña.')
            return redirect('login')
        
        backend = UsuarioBackend()  # Crear una instancia del backend
        user = authenticate(request, backend=backend, email=email, password=password)
        print('Valor de user:', user)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
            print('Error: Credenciales inválidas')
            return redirect('login')

    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def menu(request):
    user = request.user
    return render(request, 'menu.html', {'user': user}) 