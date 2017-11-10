from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save

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
    codEmprestimo = models.IntegerField("Código do Empréstimo", default=0)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    dataEmprestimo = models.DateTimeField("Data do Empréstimo")
    dataPrevDevolucao = models.DateTimeField("Data para Devolução")
    dataDevolucao = models.DateTimeField("Data de dataDevolucao", null=True, blank=True)

    def __str__(self):
        return self.livro.nome

def atualizar_livro(sender, **kwargs):
	obj = kwargs['instance']
	print(kwargs)
	if kwargs['created']:
		if sender == Emprestimo:
			novo_emprestimo = Emprestimo.objects.get(id=obj.id)
			livro = Livro.objects.get(id=novo_emprestimo.livro.id)
			livro.status = 'EMP'
			livro.codEmprestimo = novo_emprestimo.id
			livro.save()
	else:
		if sender == Emprestimo and obj.dataDevolucao != 0:
			novo_emprestimo = Emprestimo.objects.get(id=obj.id)
			livro = Livro.objects.get(id=novo_emprestimo.livro.id)
			livro.status = 'DIS'
			livro.codEmprestimo = 0
			livro.save()

post_save.connect(atualizar_livro, sender=Emprestimo)
