from django.contrib import admin
from .models import Curso, Frequencia, Turma, Solicitacao, SemestreAvaliativo, Aprovado
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

@admin.register(Solicitacao)
class SolcitacaoAdmin(admin.ModelAdmin):
    ...  

@admin.register(SemestreAvaliativo)
class SemestreAvaliativoAdmin(admin.ModelAdmin):
    ...

@admin.register(Aprovado)
class AprovadoAdmin(admin.ModelAdmin):
    ...