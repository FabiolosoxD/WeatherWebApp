from django.db import models

# Define o modelo Cidade com um campo de nome.
class Cidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
