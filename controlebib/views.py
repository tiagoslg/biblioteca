from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from controlebib.models import Livro

# Create your views here.
class Index(View):
    def get(self, request):
        livros = Livro.objects.all().order_by('id')
        context = {
    		'livros': livros,
    		}
        print(context)
        return render(request, 'controlebib/index.html', context)

class login(View):
    def post(self, request):
        m = Member.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponse(u"Você está autenticado.")
        else:
            return HttpResponse(u"Seu nome de usuário e senha não conferem.")
