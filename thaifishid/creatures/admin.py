from django.contrib import admin

from .models import Anemone, Color, Coral, Fish, Habitat, Shark


class FishAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'type')


admin.site.register(Fish, FishAdmin)
admin.site.register(Shark)
admin.site.register(Anemone)
admin.site.register(Coral)
admin.site.register(Color)
admin.site.register(Habitat)
