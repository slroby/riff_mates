from django.contrib import admin
from bands.models import Musician, Band, Venue, Room

# Register your models here.


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    pass


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    pass


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
