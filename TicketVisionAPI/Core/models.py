from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AdminsExtra(models.Model):
    cargo = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    vinculo = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user
    
class Areas(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
class Chamados(models.Model):
    nome = models.CharField(max_length=255)
    setor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    prior = models.IntegerField()
    status = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True, editable=False, blank=False)
    areas = models.ManyToManyField(Areas)
    
    def __str__(self):
        return self.nome
