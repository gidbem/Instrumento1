from django.db import models
from dateutil.relativedelta import relativedelta #precisei fazer o python -m pip install python-dateutil

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=200)
    autor = models.CharField(verbose_name='Autor', max_length=100)
    sinopse = models.TextField(verbose_name='Sinopse', blank=True, null=True)
    data_retirada = models.DateField(verbose_name='Data da retirada')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='Tags/Assuntos', blank=True)

    def __str__(self):
        return self.titulo

    @property
    def devolucao(self):
        if self.data_retirada:
            return self.data_retirada + relativedelta(months=1)
        return None




