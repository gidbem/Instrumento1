from django.db import models
from dateutil.relativedelta import relativedelta #precisei fazer o python -m pip install python-dateutil

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disponivel(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livros(models.Model):
    titulo = models.CharField('Titulo', max_length=200)
    autor = models.CharField('Autor', max_length=100)
    ano_lancamento = models.DateField('Ano de lançamento', blank=True, null=True, auto_now_add=True)
    sinopse = models.TextField('Sinopse', blank=True, null=True)
    data_retirada = models.DateTimeField('Data da retirada',auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    @property
    def devolucao(self):
        return self.data_retirada + relativedelta(months=1)




