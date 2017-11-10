from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets
from datetime import date
#from django.forms import widgets

from .models import Usuario, Emprestimo

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','email','telefone']

class EmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario','livro','dataEmprestimo','dataPrevDevolucao','dataDevolucao']
