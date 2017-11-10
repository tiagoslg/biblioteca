from django.conf.urls import url
from django.views.generic import TemplateView
from controlebib.views import Index, login

from . import views

app_name = 'controlebib'
urlpatterns = [
	url(r'^$', Index.as_view(), name="index"),
	url(r'^login/', login.as_view(), name="login"),
]
