from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import Project
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Song

# Create your views here.


def register(request):
    title = 'Nexus Music'
    if request.method == 'GET':
        return render(request, 'register.html', {
            'title': title,
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password1']
                )
                user.save()
                auth_login(request, user)
                # Agregar mensaje de depuración
                print("Redirecting to login...")
                return redirect(reverse('login'))
            except Exception as e:
                return render(request, 'register.html', {
                    'title': title,
                    'form': UserCreationForm(),
                    'error': 'Username already exists or other error: {}'.format(str(e))
                })
        else:
            return render(request, 'register.html', {
                'title': title,
                'form': UserCreationForm(),
                'error': 'Passwords do not match'
            })


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirigir al home después de un inicio de sesión exitoso
            # Asegúrate de tener una ruta definida para 'home'
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': 'Nombre de usuario o contraseña incorrectos'
            })
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'home.html', {'message': 'Bienvenido a Nexus Music'})


def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('login')


def playlist(request):
    return render(request, 'playlist.html')


def account(request):
    return render(request, 'account.html')


def search(request):
    return render(request, 'search.html')


@login_required
def studio(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist', 'Desconocido')
        audio_file = request.FILES.get('audio_file')

        if title and audio_file:
            song = Song.objects.create(
                title=title,
                artist=artist,
                audio_file=audio_file,
                uploaded_by=request.user
            )
            song.save()
            return redirect('studio')

    songs = Song.objects.filter(uploaded_by=request.user)
    return render(request, 'studio.html', {'songs': songs})


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def task(request):
    return HttpResponse("Task")
