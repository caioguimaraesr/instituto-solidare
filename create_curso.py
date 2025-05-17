import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from instsoli.models import Curso

nome = 'Iniciação a Programação'
descricao = 'Descrição para o curso de programação'

novo_curso = Curso.objects.create(
    nome=nome,
    descricao=descricao,
    imagem=None,
    documento=None
)



