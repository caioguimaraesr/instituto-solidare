from django.contrib import admin
from .models import Curso, Frequencia, Turma
# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    ...

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    ...  

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    ...  