from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    DIS = 'DIS'
    EMP = 'EMP'
    STATUS_CHOICES = (
        (DIS, 'Disponível'),
        (EMP, 'Emprestado'),
	)
    nome = models.CharField(max_length=300)
    autor = models.CharField(max_length=200, blank=True)
    editora = models.CharField(max_length=200, blank=True)
    status = models.CharField(
        max_length=3,
		choices=STATUS_CHOICES,
		default=DIS,
	)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    dataEmprestimo = models.DateTimeField(auto_now=False, auto_now_add=False)
    dataPrevDevolucao = models.DateTimeField()
    dataDevolucao = models.DateTimeField(blank=True)

    def __str__(self):
        return self.livro
