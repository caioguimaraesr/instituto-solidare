from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Curso
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'instsoli/pages/home.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'instsoli/pages/cursos/cursos.html', context={
        'cursos':cursos
    })

def detalhe_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'instsoli/pages/cursos/cursos_detalhes.html', context={
        'curso': curso
    })