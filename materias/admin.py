from django.contrib.gis import admin
from materias.models import Materia

class MateriaAdmin(admin.ModelAdmin):
    list_display = 'id_referencia', '__unicode__', 'data'
    list_filter = 'polemica', 'tramita', 'autor'
    search_fields = 'ementa', 'autor'

admin.site.register(Materia, admin.OSMGeoAdmin)
