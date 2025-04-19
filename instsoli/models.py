from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='cursos_imagens/', blank=True, null=True)
    documento = models.FileField(upload_to='documentos_cursos/', blank=True, null=True)
    
    def __str__(self):
        return self.nome