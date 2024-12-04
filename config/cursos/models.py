from django.db import models

# Create your models here.
class curso(models.Model):
   nome = models.CharField(max_length=100)
   vagas = models.IntegerField(max)
   titulo = models.CharField(max_length=100)
   descricao = models.CharField(max_length=100)
   categoria = models.CharField(max_length=100)
   conteudo = models.TextField()

   def __str__(self):
      return self.nome
   
   class Meta:
      verbose_name = "Curso"
      verbose_name_plural = "Cursos"