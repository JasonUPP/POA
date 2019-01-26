from django.shortcuts import render
from django.http import HttpResponse

from apps.usuario.forms import UsuarioForm
from apps.usuario.models import Usuario

from django.urls import path, include

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from django.shortcuts import redirect


def index(request):
	return render(request, 'index.html')

def usuario_view(request):
	if request.method == "POST":
		form= UsuarioForm(request.POST)
		if form.is_valid():
			usuario = form.save()
			return redirect('index')
	else:
		form = UsuarioForm()
	return render(request, 'usuario/formulario.html', {'form':form})

def usuario_list(request):
	usuario = Usuario.objects.all().order_by('id')
	contexto = {'usuarios':usuario}
	return render(request, 'usuario/usuario_list.html', contexto)


def usuario_edit(request, id_usuario):
	usuario = Usuario.objects.get(id=id_usuario)
	if request.method == 'GET':
		form = UsuarioForm(instance=usuario)
	else:
		form = UsuarioForm(request.POST, instance=usuario)
		if form.is_valid():
			form.save()
		return redirect('listar')
	return render(request, 'usuario/formulario.html', {'form':form})

def usuario_delete(request, id_usuario):
	usuario = Usuario.objects.get(id=id_usuario)
	if request.method == 'POST':
		usuario.delete()
		return redirect('listar')
	return render(request, 'usuario/usuario_delete.html', {'usuario':usuario})
