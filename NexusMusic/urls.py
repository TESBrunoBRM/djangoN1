from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    # Ruta para cerrar sesión
    path('playlist/', views.playlist, name='playlist'),
    path('account/', views.account, name='account'),
    path('search/', views.search, name='search'),
    path('studio/', views.studio, name='studio'),
    path('logout/', views.logout_view, name='logout'),

    path('projects/', views.projects),
    path('task/', views.task),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
