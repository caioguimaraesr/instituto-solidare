import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from instsoli.models import Curso
from django.contrib.auth.models import User
from usuario.models import InformacoesPessoais
from instsoli.models import Curso
from datetime import date

nome = 'Iniciação a Programação'
descricao = 'Descrição para o curso de programação'

novo_curso = Curso.objects.create(
    nome=nome,
    descricao=descricao,
    imagem=None,
    documento=None
)

user = User.objects.create_user(
        username='aluno_teste',
        first_name = 'Rafael',
        last_name='Ferraz',
        email='aluno@email.com',
        password='senhaSegura123'
    )

InformacoesPessoais.objects.create(
    user=user,
    cpf='123.456.789-00',
    telefone='(81) 91234-5678',
    data_nascimento=date(2000, 1, 1),
    genero='masculino',
    cep='50000-000',
    endereco='Rua Teste',
    numero='123',
    bairro='Bairro Teste',
    estado='PE',
    cidade='Recife',
    escolaridade='emc',
    escola='Escola Estadual Teste',
    turno='manha',
    curso=novo_curso
)