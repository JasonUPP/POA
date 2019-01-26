from django import forms
from apps.usuario.models import Usuario
from django.forms import ModelForm


class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = [
			'nombre',
			'apellidoP',
			'apellidoM',
			'correo',
			'password',
			'sexo',
			'edad',
			'nacimiento',
			'telefono',
			'domicilio',
		]

		CHOICES=[('Masculino','Femenino')]
		widgets= {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellidoP': forms.TextInput(attrs={'class':'form-control'}),
			'apellidoM': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.EmailInput(attrs={'class':'form-control'}),
			'password': forms.PasswordInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'edad': forms.TextInput(attrs={'class':'form-control'}),
			'nacimiento' : forms.SelectDateWidget(years=range(1920,2019),attrs={'class':'form-control'}),
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),
			'domicilio' : forms.TextInput(attrs={'class':'form-control'}),

		}