from django.contrib import admin
from .models import Project, Task, Song, Profile

# Register your models here.


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'uploaded_by', 'uploaded_at')
    search_fields = ('title', 'artist')
    list_filter = ('uploaded_at',)

    def uploaded_by(self, obj):
        return obj.user
    uploaded_by.short_description = 'Uploaded By'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')


admin.site.register(Project)
admin.site.register(Task)
