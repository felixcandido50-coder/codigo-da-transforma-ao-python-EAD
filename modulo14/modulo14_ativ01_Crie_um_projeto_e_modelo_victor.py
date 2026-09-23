'''




'''

from django.db import models

# Atividade 1: Modelo de Produto
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome