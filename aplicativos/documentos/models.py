from django.db import models
from aplicativos.funcionarios.models import Funcionario
# Create your models here.

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    owner = models.ForeignKey(Funcionario, on_delete=models.PROTECT)


    def __str__(self):
        return self.descricao

