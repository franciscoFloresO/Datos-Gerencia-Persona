from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, nombre=None):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        usuario = self.model(email=self.normalize_email(email), nombre=nombre)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password, nombre):
        usuario = self.create_user(email, password=password, nombre=nombre)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    pais = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']  # Ahora el campo 'nombre' es requerido al crear un superusuario

    def __str__(self):
        return self.email