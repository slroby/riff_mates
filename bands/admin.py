from django.contrib import admin
from bands.models import Musician, Band, Venue, Room

# Register your models here.


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_name",
        "first_name",
        "show_weekday",
    )
    search_fields = (
        "last_name",
        "first_name__startswith",
    )

    def show_weekday(self, obj):
        # Fetch weekday of artist's birth
        return obj.birth.strftime("%A")

    show_weekday.short_description = "Birth Weekday"


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    pass


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
