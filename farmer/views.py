# farmer/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import AgriculteurCreationForm

def register(request):
    if request.method == 'POST':
        form = AgriculteurCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Le compte pour {username} a été créé ! Vous pouvez maintenant vous connecter.')
            return redirect('login')
    else:
        form = AgriculteurCreationForm()
    return render(request, 'farmer/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirection vers la page d'accueil
        else:
            messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')
    return render(request, 'farmer/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté avec succès.')
    return redirect('login')

def home(request):
    return render(request, 'farmer/home.html')
