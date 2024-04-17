from django.contrib.auth.backends import BaseBackend
from .models import Usuario
from django.contrib.auth import authenticate

class UsuarioBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.check_password(password):
                print('Usuario encontrado y contraseña válida.')
                return usuario
            else:
                print('Contraseña inválida para el usuario:', email)
                return None
        except Usuario.DoesNotExist:
            print('Usuario con correo electrónico {} no encontrado.'.format(email))
            return None
        except Exception as e:
            print('Error durante la autenticación:', str(e))
            return None
    
    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            print('Usuario con ID {} no encontrado.'.format(user_id))
            return None
        except Exception as e:
            print('Error al obtener usuario por ID:', str(e))
            return None