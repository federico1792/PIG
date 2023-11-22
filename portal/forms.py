from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = User
        #User._meta.get_field('email')._unique = True
        #NO PONER '__all__', muestra todos los campos que puede tener un usuarios incluido is_staff
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {'username': ""}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Apellido',}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email',}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'