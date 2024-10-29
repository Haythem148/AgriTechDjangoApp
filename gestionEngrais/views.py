from django.shortcuts import render, redirect, get_object_or_404
from .models import Engrais, ApplicationEngrais
from .forms import EngraisForm, ApplicationEngraisForm

# List all Engrais
def engrais_list(request):
    engrais = Engrais.objects.all()
    return render(request, 'gestionEngrais/engrais_list.html', {'engrais': engrais})

# Add new fertilizer
def engrais_create(request):
    if request.method == 'POST':
        form = EngraisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('engrais-list')
    else:
        form = EngraisForm()
    return render(request, 'gestionEngrais/engrais_form.html', {'form': form})

# Edit fertilizer
def engrais_update(request, pk):
    engrais = get_object_or_404(Engrais, pk=pk)
    if request.method == 'POST':
        form = EngraisForm(request.POST, instance=engrais)
        if form.is_valid():
            form.save()
            return redirect('engrais-list')
    else:
        form = EngraisForm(instance=engrais)
    return render(request, 'gestionEngrais/engrais_form.html', {'form': form})

# Delete fertilizer
def engrais_delete(request, pk):
    engrais = get_object_or_404(Engrais, pk=pk)
    if request.method == 'POST':
        engrais.delete()
        return redirect('engrais-list')
    return render(request, 'gestionEngrais/engrais_confirm_delete.html', {'engrais': engrais})

# List all fertilizer applications
def application_engrais_list(request):
    applications = ApplicationEngrais.objects.all()
    return render(request, 'gestionEngrais/application_engrais_list.html', {'applications': applications})

# Add new fertilizer application
def application_engrais_create(request):
    if request.method == 'POST':
        form = ApplicationEngraisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application-engrais-list')
    else:
        form = ApplicationEngraisForm()
    return render(request, 'gestionEngrais/application_engrais_form.html', {'form': form})
