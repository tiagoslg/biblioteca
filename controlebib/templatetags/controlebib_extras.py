from django import template
#from django.utils.datastructures import SortedDict

register = template.Library()

@register.filter(name='status')
def statusLivro(value):
	if value == "EMP":
		return "Emprestado"
	elif value == "DIS":
		return "Disponível"
	else:
		return "Status não definido"
