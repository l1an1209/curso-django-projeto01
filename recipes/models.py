from django.db import models

class Receita(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    autor = models.CharField(max_length=100)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='receitas/', blank=True, null=True)

    def __str__(self):
        return self.titulo
