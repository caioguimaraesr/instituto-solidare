from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InformacoesPessoais(models.Model):
    PERGUNTA_CHOICES = [
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
    ]
    
    GENERO_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('pni', 'Prefiro não informar'),
    ]
    
    ESCOLARIDADE_CHOICES = [
        ('npe', 'Não possuo escolaridade'),
        ('fi', 'Fundamental Incompleto'),
        ('fc', 'Fundamental Completo'),
        ('emi', 'Ensino Médio Incompleto'),
        ('emc', 'Ensino Médio Completo'),
        ('esi', 'Ensino Superior Incompleto'),
        ('esc', 'Ensino Superior Completo'),
    ]
    
    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=100, choices=GENERO_CHOICES)
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=100, choices=ESCOLARIDADE_CHOICES)
    escola = models.CharField(max_length=100)
    turno = models.CharField(max_length=50, choices=TURNO_CHOICES)
    curso = models.ForeignKey("instsoli.Curso", on_delete=models.CASCADE)

    def __str__(self):
        return f'Informações de {self.user.username}'