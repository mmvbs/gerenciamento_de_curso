from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileExample(models.Model):

    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"