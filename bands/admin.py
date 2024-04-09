from django.contrib import admin
from bands.models import Musician

# Register your models here.


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    pass
