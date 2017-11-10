from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from controlebib.forms import EmprestimoForm
#from django.core.urlresolvers import reverse_lazy

from controlebib.models import Livro, Emprestimo, Usuario

# Create your views here.
class Index(View):
    def get(self, request):
        livros = Livro.objects.all().order_by('id')
        context = {
    		'livros': livros,
    		}
        return render(request, 'controlebib/index.html', context)


class login(View):
    def post(self, request):
        m = Member.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponse(u"Você está autenticado.")
        else:
            return HttpResponse(u"Seu nome de usuário e senha não conferem.")

class EmprestimoCreateView(CreateView):
    model = Emprestimo
    template_name = 'controlebib/emprestimo_form.html'
    form_class = EmprestimoForm
    success_url = '/reserva/sucesso/'
    def get_context_data(self, **kwargs):
        ctx = super(EmprestimoCreateView, self).get_context_data(**kwargs)
        ctx['livro_id'] = self.kwargs['livro_id']
        return ctx

class EmprestimoSucesso(View):
    def get(self, request):
        return render(request, 'controlebib/sucesso.html')

class EmprestimoUpdate(View):
    model = Emprestimo
    template_name = 'controlebib/emprestimo_update.html'
    form_class = EmprestimoForm
    success_url = '/reserva/sucesso/'
    #def get_object(self, queryset=None):
        #obj = Emprestimo.objects.get(id=self.kwargs['id'])
        #return obj
