from django.shortcuts import render
from materias.models import Materia


def home(request):
    materia_destaque = Materia.objects.all().order_by('?').first()
    materias = Materia.objects.all().exclude(id=materia_destaque.id)
    contexto = {
        'destaque': materia_destaque,
        'materias': materias
    }
    return render(request, "index.html", context=contexto)
