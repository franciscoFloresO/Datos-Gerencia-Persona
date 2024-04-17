from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):

    PAISES_CHOICES = [
        ('Chile', 'Chile'),
        ('Perú', 'Perú'),
        ('Argentina', 'Argentina'),
    ]
    
    pais = forms.ChoiceField(choices=PAISES_CHOICES)
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password','is_staff','pais']

class EditarUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmar_password = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'pais', 'is_staff', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")

        if password != confirmar_password:
            raise forms.ValidationError(
                "Las contraseñas no coinciden. Por favor, inténtalo de nuevo."
            )

        return cleaned_data