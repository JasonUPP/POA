from django import forms
from apps.anteproyecto.models import AnteProyecto
from django.forms import ModelForm

class ApForm(forms.ModelForm):
    class Meta:
        model = AnteProyecto
        fields = '__all__'
        widgets = {
        'capitulo':forms.TextInput(attrs={'class':'form-control'}),
        'partida':forms.TextInput(attrs={'class':'form-control'}),
        'enero':forms.NumberInput(attrs={'class':'form-control'}),
        'febrero':forms.NumberInput(attrs={'class':'form-control'}),
        'marzo':forms.NumberInput(attrs={'class':'form-control'}),
        'abril':forms.NumberInput(attrs={'class':'form-control'}),
        'mayo':forms.NumberInput(attrs={'class':'form-control'}),
        'junio':forms.NumberInput(attrs={'class':'form-control'}),
        'julio':forms.NumberInput(attrs={'class':'form-control'}),
        'agosto':forms.NumberInput(attrs={'class':'form-control'}),
        'septiembre':forms.NumberInput(attrs={'class':'form-control'}),
        'octubre':forms.NumberInput(attrs={'class':'form-control'}),
        'noviembre':forms.NumberInput(attrs={'class':'form-control'}),
        'diciembre':forms.NumberInput(attrs={'class':'form-control'}),
        'total':forms.NumberInput(attrs={'class':'form-control'}),
        }
