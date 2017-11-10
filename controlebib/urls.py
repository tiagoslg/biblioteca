from django.conf.urls import url
from django.views.generic import TemplateView
from controlebib.views import Index, login, EmprestimoCreateView, EmprestimoSucesso, EmprestimoUpdate

from . import views

app_name = 'controlebib'
urlpatterns = [
	url(r'^$', Index.as_view(), name="index"),
	url(r'^login/', login.as_view(), name="login"),
	url(r'^(?P<livro_id>[0-9]+)/$', EmprestimoCreateView.as_view(), name='criarEmprestimo'),
	url(r'^reserva/sucesso/$', EmprestimoSucesso.as_view(), name='reservaSucesso'),
	#url(r'^admin/controlebib/emprestimo/(?P<idEmprestimo>[0-9]+)/change/$', EmprestimoUpdate.as_view(), name='atualizarEmprestimo'),
]
