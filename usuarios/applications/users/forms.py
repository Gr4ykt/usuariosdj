from django import forms
from .models import User
from django.contrib.auth import authenticate

class UserRegisterform(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password'
            }
        )
    )

    RepetirPassword = forms.CharField(
        label='Repita Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Password'
            }
        )
    )

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User        
        fields = (
                'username',
                'email',
                'nombres',
                'apellidos',
                'genero',
            )

    def clean_RepetirPassword(self):
        if self.cleaned_data['password1'] != self.cleaned_data['RepetirPassword']:
            self.add_error('RepetirPassword', 'Las password no son las mismas')

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data

class UpdatePasswordForm(forms.Form):
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
        }))
    
class VerificationForm(forms.Form):
    codregistro = forms.CharField(required=True)
