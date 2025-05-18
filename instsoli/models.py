from django.db import models
from usuario.models import InformacoesPessoais
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='cursos_imagens/', blank=True, null=True)
    documento = models.FileField(upload_to='documentos_cursos/', blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    alunos = models.ManyToManyField(InformacoesPessoais, blank=True)

    def _str_(self):
        return f'{self.nome} - {self.curso.nome}'
    
class Frequencia(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(InformacoesPessoais, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=True)

    class Meta:
        unique_together = ('turma', 'aluno', 'data')

    def __str__(self):
        return f"{self.aluno.user.username} - {self.data} - {'Presente' if self.presente else 'Faltou'}"
    
class Aviso(models.Model):
    PRIORIDADE_CHOICES = [
        ('normal', 'Normal'),
        ('importante', 'Importante'),
        ('urgente', 'Urgente'),
    ]

    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    mensagem = models.TextField()
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='normal')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Solicitacao(models.Model):
    TIPO_CHOICES = [
        ('duvida', 'Dúvida'),
        ('problema', 'Problema'),
        ('sugestao', 'Sugestão'),
        ('outro', 'Outro'),
    ]
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('resolvido', 'Resolvido'),
    ]

    titulo = models.CharField(max_length=100)
    mensagem = models.TextField(default='')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes_enviadas')
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes_recebidas', null=True, blank=True)
    solucao_resposta = models.TextField(default='')
    arquivada = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'
        ordering = ['-data_criacao']
    
    def arquivar(self):
        self.arquivada = True
        self.save()

    def clean(self):
        if self.pk:
            old_status = Solicitacao.objects.get(pk=self.pk).status
            if old_status in ['em_andamento', 'resolvido'] and self.status == 'pendente':
                raise ValidationError("Não é possível voltar para 'pendente' após o atendimento iniciado.")
        super().clean()

    def __str__(self):
        return f"{self.titulo} - {self.get_status_display()}"