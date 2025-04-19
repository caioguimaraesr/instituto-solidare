from django.contrib import admin
from .models import InformacoesPessoais
# Register your models here.
@admin.register(InformacoesPessoais)
class InformacoesPessoaisAdmin(admin.ModelAdmin):
    ...