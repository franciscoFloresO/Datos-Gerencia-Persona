from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm, EditarUsuarioForm
from .models import Usuario

def crear_usuario(request):
    user = request.user
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Obtén los datos del formulario
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            pais = form.cleaned_data['pais'] 
            password = form.cleaned_data['password']
            
            # Hashea la contraseña antes de guardar el usuario
            hashed_password = make_password(password)
            
            # Guarda el usuario en la base de datos
            usuario = form.save(commit=False)
            usuario.password = hashed_password
            usuario.save()
            
            return redirect('menu')  # Redirige a la página que quieras después de crear el usuario
        else:
            print('Errores en el formulario:', form.errors)
            return HttpResponse('Errores en el formulario. Revisa la consola para más detalles.')
    else:
        form = UsuarioForm()
    return render(request, 'crear_usuario.html', {'form': form})

def lista_usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuario.html',{'usuarios':usuarios})


def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:  # Si se proporcionó una nueva contraseña
                usuario.set_password(password)  # Establece la contraseña con hash
            usuario.save()
            return redirect('menu')  # Redirige a la página que quieras después de editar el usuario
    else:
        form = EditarUsuarioForm(instance=usuario)
    
    return render(request, 'editar_usuario.html', {'form': form})