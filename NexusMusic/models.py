from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='songs/')
    cover_image = models.ImageField(
        upload_to='covers/', blank=True, null=True)  # Nuevo campo
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    decription = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
