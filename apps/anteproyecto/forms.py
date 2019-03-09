from django import forms
from django.forms import ModelForm
from apps.anteproyecto.models import *

class ApForm(forms.ModelForm):
    class Meta:
        model = AnteProyecto
        fields = {'nombre', 'user'}
        widgets = {
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        'user': forms.Select(attrs={'class':'form-control'}),
        'estadoN': forms.Select(attrs={'class':'form-control'}),
        }

class FilaForm(forms.ModelForm):
    class Meta:
        model = Fila
        fields = ('anteProyecto', 'capitulo', 'concepto', 'partidagenerica', 'partidaespecifica','enero', 'febrero', 'marzo',
        'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre', 'totalF')

        widgets = {
        'anteProyecto': forms.Select(attrs={'class':'form-control'}),
        'capitulo': forms.Select(attrs={'class':'form-control'}),
        'concepto': forms.Select(attrs={'class':'form-control'}),
        'partidagenerica': forms.Select(attrs={'class':'form-control'}),
        'partidaespecifica': forms.Select(attrs={'class':'form-control'}),
        'enero':forms.NumberInput(),
        'febrero':forms.NumberInput(),
        'marzo':forms.NumberInput(),
        'abril':forms.NumberInput(),
        'mayo':forms.NumberInput(),
        'junio':forms.NumberInput(),
        'julio':forms.NumberInput(),
        'agosto':forms.NumberInput(),
        'septiembre':forms.NumberInput(),
        'octubre':forms.NumberInput(),
        'noviembre':forms.NumberInput(),
        'diciembre':forms.NumberInput(),
        }

class CapituloForm(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = {'numero'}
        widgets = {
        'numero':forms.NumberInput(attrs={'class':'form-control'}),
        }

class ConceptoForm(forms.ModelForm):
    class Meta:
        model = Concepto
        fields = {'numero','capitulo'}
        widgets = {
        'numero':forms.NumberInput(attrs={'class':'form-control'}),
        'capitulo': forms.Select(attrs={'class':'form-control'}),
        }

class PGForm(forms.ModelForm):
    class Meta:
        model = PartidaGenerica
        fields = {'numero','concepto'}
        widgets = {
        'numero':forms.NumberInput(attrs={'class':'form-control'}),
        'concepto': forms.Select(attrs={'class':'form-control'}),
        }

class PEForm(forms.ModelForm):
    class Meta:
        model = PartidaEspecifica
        fields = {'numero','nombre','descripcion','partidaGenerica'}
        widgets = {
        'numero':forms.NumberInput(attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        'partidaGenerica': forms.Select(attrs={'class':'form-control'}),
        }
