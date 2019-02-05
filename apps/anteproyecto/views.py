from django.shortcuts import render
from apps.anteproyecto.forms import ApForm
from apps.anteproyecto.models import AnteProyecto

def inicio(request):
    return render(request, 'ap/anteproyecto.html', {})

def crearap(request):
    if request.method == "POST":
        form = ApForm(request.POST)
        if form.is_valid():
            ap = form.save()
            return redirect('AnteProyecto')
    else:
        form = ApForm()
    return render(request, 'ap/crearap.html', {'form':form})

def insertarap(request):
    return render(request, 'ap/insertarap.html', {})

def fd(request):
    return render(request, 'ap/fd.html', {})
